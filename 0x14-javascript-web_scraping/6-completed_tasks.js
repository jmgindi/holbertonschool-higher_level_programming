#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let completed = {};
    for (let i = 0; i < JSON.parse(body).length; i++) {
      if (JSON.parse(body)[i].completed) {
        if (!(JSON.parse(body)[i].userId in completed)) {
          completed[JSON.parse(body)[i].userId] = 1;
        } else {
          completed[JSON.parse(body)[i].userId]++;
        }
      }
    }
    console.log(completed);
  }
});
