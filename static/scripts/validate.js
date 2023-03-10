let form = document.querySelector("form")
form.addEventListener('submit', function(e){
    e.preventDefault()
    var valid = true

    r1 = checkText(scoreForm.fName, 2, 100, $('#fNameError'))
    r2 = checkText(scoreForm.lName, 2, 100, $('#lNameError'))
    r3 = checkText(scoreForm.grade, 1, 50, $('#gradeError'))
    r4 = checkList($('#course'), $('#courseError'))
    r5 = checkList($('#work'), $('#workError'))

    valid = r1 && r2 && r3 && r4 && r5
    if (valid) {
        $(this).unbind('submit').submit()
    }
})

/////////////////////////////////////////////////////////////

function checkText(field, min, max, element) {
    var valid
    if (field.value === '') {
        $(element).text("Should not be null")
        valid = false
    }
    else if (field.value.length < min) {
        $(element).text("Should not less than " + min)
        valid = false
    }
    else if (field.value.length > max) {
        $(element).text("Should not longer than " + max)
        valid = false
    }
    else {
        valid = true
    }
    return valid
}

function checkList(droplist, alertElement) {
    var valid
    if ($(droplist).prop('selectedIndex') <= 0) {
        $(alertElement).text("Please select 1 option")
        valid = false
    }
    else {
        valid = true
    }
    return valid
}
