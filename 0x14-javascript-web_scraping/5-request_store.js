#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(res.statusCode);
  }
});
