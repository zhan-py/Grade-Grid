$("#fName").blur(function() {
    textEvent(scoreForm.fName, 2, 100, $('#fNameError'))
})

$("#lName").blur(function() {
    textEvent(scoreForm.lName, 2, 100, $('#lNameError'))
})

$("#grade").blur(function() {
    textEvent(scoreForm.grade, 1, 100, $('#gradeError'))
})

$("#course").blur(function() {
    listEvent($('#course'), $('#courseError'))
})

$("#work").blur(function() {
    listEvent($('#work'), $('#workError'))
})


function textEvent(field, min, max, alertEle) {
    if (field.value !== "" && field.value.length >= min && field.value.length <= max) {
        $(alertEle).text("");
        $(field).css("background-color", "#E8F0FE")
    }
    else if (field.value !== "" && field.value.length < min) {
        $(alertEle).text("Please input with length no less than " + min + '.');
    }
    else if (field.value !== "" && field.value.length > max) {
        $(alertEle).text("Please input with length no more than " + max + '.');
    }
}

function listEvent(droplist, alertElement) {
    if ($(droplist).prop('selectedIndex') > 0) {
        $(alertElement).text("")
        $(droplist).css("background-color", "#E8F0FE")

    }
}

//////////////////////////////////////////////////////////////////////////////////////////
let position = 0;

function vivaFlorValor() {
    position = position+6;
    $("header img").css({'transform' : 'rotate('+ position +'deg)'});
}

var flor = setInterval(vivaFlorValor, 1000);