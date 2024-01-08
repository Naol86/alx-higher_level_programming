#!/usr/bin/node

const { argv } = require('node:process');

const leng = argv.length;

if (leng === 1) {
  console.log('No argument');
} else if (leng === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
