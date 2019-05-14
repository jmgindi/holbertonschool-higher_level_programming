#!/usr/bin/node
const fs = require('fs');
let filePath = process.argv[2];
let writeString = process.argv[3];
fs.writeFile(filePath, writeString, function (err) {
  if (err) {
    console.log(err);
  }
});
