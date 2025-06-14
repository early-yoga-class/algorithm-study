const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(input[0]);
const arr = input[1].split(" ").map(e => Number(e));

// 정답 배열 초기화
let answer = Array.from({ length: N }, () => -1);
let stack = [0];

// 원소의 idx stack push
// top보다 작으면 오큰수 X => idx push
// top 보다 크면 오큰수 O => 자신보다 큰 수들 pop 하고 자신 추가
for (let i = 1; i < N; i++) {
  while (arr[stack[stack.length - 1]] < arr[i] && stack.length) {
    answer[stack.pop()] = arr[i];
  }
  stack.push(i);
}

console.log(answer.join(" "));