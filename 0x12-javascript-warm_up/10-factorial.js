#!/usr/bin/node

function Factorial (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  }
  return x * Factorial(x - 1);
}

const argv = process.argv;
console.log(Factorial(parseInt(argv[2])));
