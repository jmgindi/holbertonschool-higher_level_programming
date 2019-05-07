#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  console.log(process.argv.sort((a, b) => a - b).reverse()[1]);
}
