const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split('\n');

let S = input[0];
let T = input[1];

function DFS(T) {
  if (S === T) return 1;
  if (T.length === 0) return 0;

  if (T[T.length - 1] === 'A') {
    if (DFS(T.slice(0, -1)) === 1) return 1;
  }

  if (T[0] === 'B') {
    if (DFS(T.split('').reverse().slice(0, -1).join('')) === 1) return 1;
  }

  return 0;
}

console.log(DFS(T));
