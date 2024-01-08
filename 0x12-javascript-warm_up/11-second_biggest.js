#!/usr/bin/node

const argv = process.argv;

if (argv[2] === undefined || argv[3] === undefined) {
  console.log(0);
} else {
  const arr = [-Number.MAX_VALUE, -Number.MAX_VALUE];
  let i;
  let temp;
  for (i = 2; i < argv.length; i++) {
    temp = parseInt(argv[i]);
    if (arr[1] < temp) {
      arr[0] = arr[1];
      arr[1] = temp;
    } else if (arr[0] < temp) {
      arr[0] = temp;
    }
  }
  console.log(arr[0]);
}
