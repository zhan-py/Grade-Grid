#don't use sqlite3 as file name!!
import sqlite3
from sqlite3 import Error

def create_connection(DBName):
    conn = None
    try:
        conn = sqlite3.connect(DBName)  # returns a Connection object that represents the database
        print(sqlite3.version)
        print("test0", conn)  # test0 <sqlite3.Connection object at 0x000001D431F467B0>
    except sqlite3.Error as e:
        print(e)
    return conn  # important!! when return and when don't return???


def createTable(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def startCreating():
    database = "score"
    sql_create_scores_table = """CREATE TABLE IF NOT EXISTS scores (
                                        id integer PRIMARY KEY,
                                        fName text NOT NULL,
                                        lName text NOT NULL,
                                        course text NOT NULL,
                                        work_type text NOT NULL,
                                        grade text NOT NULL
                                        primary key(id, fName, lName, course, work_type)
                                    ); """
    conn = create_connection(database)
    print("test", conn)  # test None, without return in create_connection() before hand

    if conn is not None:
        createTable(conn, sql_create_scores_table)
    else:
        print("Error happened!")

startCreating()