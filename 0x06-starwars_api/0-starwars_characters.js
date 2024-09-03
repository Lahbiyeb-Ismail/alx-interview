#!/usr/bin/node

const request = require("request");

if (process.argv.length !== 3) {
	console.error("Usage: node script.js <Movie ID>");
	process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = "https://swapi-api.alx-tools.com/api/films/" + movieId;

request(apiUrl, (err, _res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const characters = JSON.parse(body).characters;
  getMovieCharacter(characters, 0);
});

const getMovieCharacter = (characters, index) => {
  if (characters.length === index) return;
  
  request(characters[index], (err, _res, body) => {
    if (err){
      console.log(err)
      return;
    }

    console.log(JSON.parse(body).name);
    getMovieCharacter(characters, index + 1);
  });
};
