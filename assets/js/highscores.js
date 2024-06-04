#!/usr/bin/node
const highScoresList = document.getElementById("highScoresList");
//const highScores = JSON.parse(localStorage.getItem("highScores")) || [];

fetch('http://localhost:5000/users')
	.then((res) => {
		return res.json();
	})
	.then((highScores) => {
		highScoresList.innerHtml = highScores
			.map(score => {
				return `<li class="high-score">${score.username} - ${score.score}</li>`;
			})
			.join("");
	});
//highScoresList.innerHTML = highScores
  //.map(score => {
    //return `<li class="high-score">${score.name} - ${score.score}</li>`;
  //})
//  .join("");
