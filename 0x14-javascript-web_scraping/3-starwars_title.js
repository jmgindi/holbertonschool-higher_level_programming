#!/usr/bin/node
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(res.statusCode);
  }
});
