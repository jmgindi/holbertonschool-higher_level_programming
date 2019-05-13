#!/usr/bin/node
const S = require('./5-square')

module.exports = class Square extends S {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width))
    }
  }
};
