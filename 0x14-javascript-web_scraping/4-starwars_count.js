#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    let films = JSON.parse(body).results;
    let nbFilms = 0;
    for (let i = 0; i < films.length; i++) {
      for (let c = 0; c < films[i].characters.length; c++) {
        if (films[i].characters[c].includes('18')) {
          nbFilms++;
        }
      }
    }
    console.log(nbFilms);
  } else {
    console.log(res.statusCode);
  }
});
