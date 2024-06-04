#!/usr/bin/node
const username = document.getElementById('username');
const saveScoreBtn = document.getElementById('saveScoreBtn');
const finalScore = document.getElementById('finalScore');
const mostRecentScore = localStorage.getItem('mostRecentScore');

const highScores = JSON.parse(localStorage.getItem('highScores')) || [];

const MAX_HIGH_SCORES = 5;

finalScore.innerText = mostRecentScore;

username.addEventListener('keyup', () => {
	saveScoreBtn.disabled = !username.value;
});

saveHighScore = (e) => {
	e.preventDefault();
	
	const score = {
		score: mostRecentScore,
		name: username.value,
	};

	fetch('http://localhost:5000/users', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(score)
	}).then(() => {
		window.location.assign('indes.html');
	});
};
    
//highScores.push(score);
    //highScores.sort((a, b) => b.score - a.score);
    //highScores.splice(5);

    //localStorage.setItem('highScores', JSON.stringify(highScores));
  //  window.location.assign('/');
//};
