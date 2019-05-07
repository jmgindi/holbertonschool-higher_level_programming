#!/usr/bin/node
if (process.argv[2] && Number(process.argv[2])) {
  for (let h = 0; h < process.argv[2]; h++) {
    let row = '';
    for (let w = 0; w < process.argv[2]; w++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
