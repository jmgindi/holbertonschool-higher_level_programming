#!/usr/bin/node
module.exports.esrever = function (list) {
  var newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
