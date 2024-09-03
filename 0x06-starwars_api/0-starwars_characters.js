#!/usr/bin/node

const request = require("request");

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (_error, _response, body) => {
	const movieData = JSON.parse(body);
	const characterUrls = movieData.characters;

	for (const characterUrl of characterUrls) {
		request(characterUrl, (_error, _response, body) => {
			const characterData = JSON.parse(body);
			console.log(characterData.name);
		});
	}
});
