#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let hei = 0; hei < this.height; hei++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    let x = this.width;
    this.width = this.height;
    this.height = x;
  }
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
