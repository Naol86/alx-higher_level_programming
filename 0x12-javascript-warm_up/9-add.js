#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const argv = process.argv;

if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log('NaN');
} else {
  add(parseInt(argv[2]), parseInt(argv[3]));
}
