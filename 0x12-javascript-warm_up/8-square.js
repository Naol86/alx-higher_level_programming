#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
