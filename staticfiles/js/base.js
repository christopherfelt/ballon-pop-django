
/*jshint esversion: 6 */

//#region GAME LOGIC AND DATA

// DATA
let clickCount = 0;
let height = 120;
let width = 100;
let inflationRate = 20;
let maxSize = 300;
let highestPopCount = 0;
let currentPopCount = 0;
let gameLength = 5000;
let clockId = 0;
let timeRemaining = 0;
let currentPlayer = {};
let currentColor = "red";
let possibleColors = ["red", "green", "blue", "purple", "pink"];

function startGame() {
  document.getElementById("game-controls").classList.remove("hidden");
  document.getElementById("main-controls").classList.add("hidden");

  startClock();
  setTimeout(stopGame, gameLength);
}

function startClock() {
  timeRemaining = gameLength;
  drawClock();
  clockId = setInterval(drawClock, 1000);
}

function stopClock() {
  clearInterval(clockId);
}

function drawClock() {
  let countDownElem = document.getElementById("countdown");
  countDownElem.innerText = (timeRemaining / 1000).toString();
  timeRemaining -= 1000;
}

function inflate() {
  clickCount++;
  height += inflationRate;
  width += inflationRate;

  checkBalloonPop();

  draw();
}

function checkBalloonPop() {
  if (height >= maxSize) {
    console.log("pop the balloon");
    let balloonElement = document.getElementById("balloon");
    balloonElement.classList.remove(currentColor);
    getRandomColor();
    balloonElement.classList.add(currentColor);

    // @ts-ignore
    document.getElementById("pop-sound").play();

    currentPopCount++;
    height = 0;
    width = 0;
  }
}

function getRandomColor() {
  let i = Math.floor(Math.random() * possibleColors.length);
  currentColor = possibleColors[i];
}

function draw() {
  let balloonElement = document.getElementById("balloon");
  let clickCountElem = document.getElementById("click-count");

  balloonElement.style.height = height + "px";
  balloonElement.style.width = width + "px";

  clickCountElem.innerText = clickCount.toString();

}

function stopGame() {
  console.log("Game Over");

  document.getElementById("main-controls").classList.remove("hidden");
  document.getElementById("game-controls").classList.add("hidden");

  clickCount = 0;
  height = 120;
  width = 100;

  saveScore();

  currentPopCount = 0;

  stopClock();
  draw();
}

//#endregion

//#region SAVE SCORE
function saveScore(){

  let scoreData = getScoreData();

  fetch(saveScoreUrl, {
    method: 'POST',
    header: {'Content-Type':'application/x-www-form-urlencoded'},
    body: scoreData,
  }).then((response)=> {
    if(response.status == 200){
      console.log(response.json());
    } 
  });
}

function getScoreData(){

  let formData = new FormData;
  let csrftoken = getCookie('csrftoken');
  formData.append('csrfmiddlewaretoken',csrftoken);
  formData.append('score', currentPopCount);

  return formData;

}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//#endregion