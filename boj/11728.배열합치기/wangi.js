const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [N, M] = input[0].split(' ').map(Number);
let array_A = input[1].split(' ').map(Number);
let array_B = input[2].split(' ').map(Number);

let result = [...array_A, ...array_B];
result.sort((a, b) => a - b);

console.log(result.join(' '));