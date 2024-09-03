#!/usr/bin/node

const request = require("request");

if (process.argv.length !== 3) {
	console.error("Usage: node script.js <Movie ID>");
	process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = "https://swapi-api.alx-tools.com/api/films/" + movieId;

request(apiUrl, (error, _response, body) => {
	if (error) {
		console.error("Error fetching movie data:", error);
		return;
	}

	const movieData = JSON.parse(body);
	const characterUrls = movieData.characters;

	for (const characterUrl of characterUrls) {
		request(characterUrl, (error, _response, body) => {
			if (error) {
				console.error("Error fetching character data:", error);
				return;
			}

			const characterData = JSON.parse(body);
			console.log(characterData.name);
		});
	}
});
