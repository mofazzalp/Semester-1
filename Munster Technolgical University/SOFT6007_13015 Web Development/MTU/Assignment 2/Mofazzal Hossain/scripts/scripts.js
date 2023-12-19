// Author of all images: Paul Davey, http://mattahan.deviantart.com/
// License: https://creativecommons.org/licenses/by-nc-sa/3.0/

// Declare global variables to shorten code and improve readability
var image = document.getElementById("logo"),
    avenger = document.getElementById("avenger"),
    displayFav = document.getElementById("displayFav"),
    findOutButton = document.getElementById("findOutButton"),
    playButton = document.getElementById("playButton");

// This function will toggle the dropdown menu
function displayMenu() {
    var menu = document.getElementById("expandingMenu");

    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

// This function changes colour and text based on how the user rates the website using a slider.
function slide() {
    var slider = document.getElementById("rateWebsite"),
        opinion = document.getElementById("opinion"),
        userOpinion = slider.value;

    if (userOpinion == 0) {  // A different string and colour based on user rating
        opinion.innerHTML = "Very bad!";
        opinion.style.color = "lightpink";
    } else if (userOpinion == 1) {
        opinion.innerHTML = "bad!";
        opinion.style.color = "orange";
    } else if (userOpinion == 2) {
        opinion.innerHTML = "Alright!";
        opinion.style.color = "yellow";
    } else if (userOpinion == 3) {
        opinion.innerHTML = "Decent!";
        opinion.style.color = "lime";
    } else if (userOpinion == 4) {
        opinion.innerHTML = "Good!";
        opinion.style.color = "lightgreen";
    } else {
        opinion.innerHTML = "Amazing!";
        opinion.style.color = "gold";
    }
}

function changeLogo() {
    image.src = "images/A-256.png";
    // https://www.pngegg.com/en/search?q=marvel+Studios
}

function revertLogo() {
    image.src = "images/marvel.png";
}

// This function takes user input and displays their selection on screen
function displayUserText() {
    var submitButton = document.getElementById("submitButton"),
        userFav = document.getElementById("userFav");

    displayFav.innerHTML = userFav.value;

    submitButton.style.display = "none"; 
    playButton.style.display = "inline";
}
function displayBio() {
    var number = Math.floor(Math.random() * 5), 
        bio = document.getElementById("bio"),
        heroName = document.getElementById("name"),
        actor = document.getElementById("actor"),
        heroImage = document.getElementById("heroImg");

    if (number === 0) {
        league.innerHTML = "Marvel Univers";
        avenger.innerHTML = "Iron Man";
        heroName.innerHTML = "Tony Stark";
        actor.innerHTML = "Robert Downey Jr.";
        heroImage.src = "images/im.png";
    } else if (number === 1) {
        league.innerHTML = "Marvel Univers";
        avenger.innerHTML = "Captain America";
        heroName.innerHTML = "Steve Rogers";
        actor.innerHTML = "Chris Evans";
        heroImage.src = "images/ca.png";
    } else if (number === 2) {
        league.innerHTML = "Marvel Univers";
        avenger.innerHTML = "Hulk";
        heroName.innerHTML = "Bruce Banner";
        actor.innerHTML = "Mark Ruffalo";
        heroImage.src = "images/hulk.png";
    } else if (number === 3) {
        league.innerHTML = "DC Universe";
        avenger.innerHTML = "Aquaman";
        heroName.innerHTML = "Arthur Curry";
        actor.innerHTML = "Jason Momoa";
        heroImage.src = "images/aqu.png";
    } else if (number === 4) {
        league.innerHTML = "DC Universe";
        avenger.innerHTML = "Batman";
        heroName.innerHTML = "Bruce Wayne";
        actor.innerHTML = "Robert Pattinson";
        heroImage.src = "images/batman.png";
    }else {
        league.innerHTML = "DC Universe";
        avenger.innerHTML = "Superman";
        heroName.innerHTML = "Clark Kent";
        actor.innerHTML = "Henry Cavill";
        heroImage.src = "images/superman.png";
    }

    bio.style.display = "block";  // Display bio
    playButton.style.display = "none";  // Remove option to play
    findOutButton.style.display = "inline";  // Allow user to check if their answer was correct
}

// This function compares user submitted string to the characted selcted in the previous function
function checkValues() {
    var guessText = document.getElementById("displayGuess");

    if (avenger.innerHTML === displayFav.innerHTML) {  // When values match user is congratulated
        guessText.innerHTML = "Well Done! You guessed correct!";
        guessText.style.color = "green";
    } else {  // If the user is wrong they get a message of encouragement
        guessText.innerHTML = "Nope! Better luck next time!";
        guessText.style.color = "red";
    }

    findOutButton.style.display = "none";  // Remove option to "find out"
    guessText.style.display = "inline";  // Display text
}
