#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number is: ' + num);
}
