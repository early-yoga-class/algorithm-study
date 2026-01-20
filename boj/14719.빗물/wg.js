const fs = require("fs")
const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().split('\n');

const [H, W] = input[0].split(' ').map(Number)
const pillars = input[1].split(' ').map(Number)

let left = 0
let right = W - 1
let left_h = 0
let right_h = 0

let rain = 0

while (left < right) {
  if (pillars[left] <= pillars[right]) {
    left_h = Math.max(left_h, pillars[left])
    rain += left_h - pillars[left]
    left += 1
  } else {
    right_h = Math.max(right_h, pillars[right])
    rain += right_h - pillars[right]
    right -= 1
  }
}

console.log(rain)