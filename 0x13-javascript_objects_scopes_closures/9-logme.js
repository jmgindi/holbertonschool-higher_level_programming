#!/usr/bin/node
let args = 0;
module.exports.logMe = function (item) {
  console.log(args + ': ' + item);
  args++;
};
