/*  ### homeWork ####
 
 1. Full name greeting. Write a program that asks for a person’s first name, then middle, 
    and then last. Finally, it should greet the person using their full name. name

 2. Bigger, better favorite number. Write a program that asks for a person’s favorite number. 
    Have your program add 1 to the number, and then suggest the result as 
    a bigger and better favorite number. (Do be tactful about it, though.)

 3. Angry boss. Write an angry boss program that rudely asks what you want. 
    Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this: 
    WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!


 4. Table of contents. Here’s something for you to do in order to play around more with center, 
    ljust, and rjust: write a program that will display a table of contents so that it looks like
    this:   
    Table of Contents 
    
    Chapter 1: Getting Started        page 1
    Chapter 2: Numbers                page 9
    Chapter 3: Letters                page 13

    Optional: in JS we may prefer to 'print' these to the HTML file itself rather than the console.
*/

/* How to define functions in JS:
        function name(parameter1, parameter2, parameter3) {
        code to be executed
}*/


// 1.

function fullNameGreeting() {
    
    var firstName = prompt("What's your first name?");
    var lastName = prompt("What's your last name?");
    alert("Hello " + firstName + " " + lastName + "!");     
}

var startButton = document.getElementById("button");
startButton.addEventListener("click", fullNameGreeting);


/* 

A.) solution

function fng(){
var retval = "Helo "    
retval += prompt("What's your first name?") + " ";
retval += prompt("What's your last name?") + "!";
alert(retval);     
}
var x = document.getElementById("button");
x.addEventListener("click", fng);

#####################################################################

B.) solution

var startButton = document.getElementById("button");
startButton.addEventListener("click", function () {
    var firstName = prompt("What's your first name?");
    var lastName = prompt("What's your last name?");
    alert("Hello " + firstName + " " + lastName + "!");     
});

*/

// 2. 

function biggerNum(){
    alert("event ok");
    var userNum = inputField.value;
    inputField.value = "";
    alert("I suggest you a bigger and better number: " + (parseInt(userNum) + 1));
}

var inputField = document.getElementById("input");
inputField.addEventListener("change", biggerNum);


// 3.

function angryBoss(){
    var ask = document.getElementById("angry_input").value;
    alert("WADDAYA MEAN ON '" + ask + "'?!\nYou are FIRED!!!!");
}

document.getElementById("angry_input").addEventListener("change", angryBoss);
