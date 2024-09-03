#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

const fetchStarWars = (charList, index) => {
  if (charList.length === index) return;
  request(charList[index], (err, res, body) => {
    if (err) console.log(err);
    else {
      console.log(JSON.parse(body).name);
      fetchStarWars(charList, index + 1);
    }
  });
};

request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const charList = JSON.parse(body).characters;
    fetchStarWars(charList, 0);
  }
});
