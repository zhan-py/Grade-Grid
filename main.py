from flask import Flask, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("score")
    c = conn.cursor()
    c.execute('select distinct course from scores')
    allCourse = c.fetchall()
    allCourseList = [course[0] for course in allCourse]

    c.execute('select distinct work_type from scores')
    allWorkType = c.fetchall()
    allWorkTypeList = [work[0] for work in allWorkType]

    conn.close()
    return render_template("index.html", allCourseList = allCourseList, allWorkTypeList = allWorkTypeList)


gradeDetails = '''
                      SELECT id, fName, lName, course, work_type, grade, grade_processed, 
                      case when grade_processed >= 80 then 'A' when grade_processed >= 70 then 'B'
                      when grade_processed >= 60 then 'C' when grade_processed >= 50 then 'D' 
                      else 'F' end as 'letter_grade'
                      FROM scores
                      '''


finalLetterGrade = '''select fName, lName, course, case when grade_weighted_avg >= 80 then 'A' when grade_weighted_avg >= 70 then 'B'
                      when grade_weighted_avg >= 60 then 'C' when grade_weighted_avg >= 50 then 'D' 
                      else 'F' end as 'letter_grade' 
                      from (
                          SELECT fName, lName, course, round(sum(weight*grade_processed), 1) as grade_weighted_avg
                          from (
                                SELECT id, fName, lName, course, case when work_type = "Assignments" then 0.4
                                when work_type = "Midterms" then 0.35 
                                when work_type = "Final" then 0.25 else '' end as 'weight', grade_processed
                                FROM scores
                                ) t
                          group by fName, lName, course
                      ) t1
                      where fName || lName || course in (
                        select fName || lName || course from (
                                SELECT fName, lName, course, length(GROUP_CONCAT(work_type)) as 'work_type_len'
                                FROM scores                      
                                group by fName, lName, course    
                                having work_type_len = 26                        
                              ) T
                      )
                      '''
                      
                      
@app.route("/display")
def display():
    conn = sqlite3.connect("score")
    c = conn.cursor()
    c.execute(gradeDetails)
    allRecDetail = c.fetchall()

    c.execute(finalLetterGrade)
    allRecSum = c.fetchall()

    conn.close()
    return render_template("display.html", allRecSum=allRecSum, allRecDetail=allRecDetail)


@app.route("/display", methods=["POST", "GET"])
def inputAndDisplay():
    if request.method == 'POST':
        result = request.form
        rec = []
        for k,v in result.to_dict().items():
            rec.append(v)

        scoreProcessSplit = (rec[-1].replace('(', "").replace(')', "")).split(", ")
        scoreProcessToInt = [int(el) for el in scoreProcessSplit]
        scoreProcessAvgScore = round(sum(scoreProcessToInt)/len(scoreProcessToInt), 1)

        rec.append(scoreProcessAvgScore)
        record = tuple(rec)

        ###############################################################
        conn = sqlite3.connect("score")
        c = conn.cursor()
        c.execute('''
                insert into scores (fName, lName, course, work_type, grade, grade_processed)
                values''' + str(record)
                  )
        conn.commit()

        ###############################################################
        c.execute(gradeDetails)
        allRecDetail = c.fetchall()

        c.execute(finalLetterGrade)
        allRecSum = c.fetchall()

        conn.close()
        return render_template("display.html", allRecDetail = allRecDetail, allRecSum = allRecSum)

if __name__ == "__main__":
    app.run(debug=True)
