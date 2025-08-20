let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim();
// let input = fs.readFileSync("/dev/stdin").toString().trim();

let N = Number(input);

let result = [];

// (i, j)는 좌표, num은 현재 보는 전체 패턴의 크기
const star = (i, j, num) => {
  // 3일경우 가운데 1*1 공백
  if (i % 3 === 1 && j % 3 === 1) {
    result.push(" ");
  } else {
    // 가운데 아닌 경우
    if (num === 1) {
      result.push("*");
    } else {
      // 재귀, i, j, Num 3으로 쪼개어 재귀 실행
      star(parseInt(i / 3), parseInt(j / 3), parseInt(num / 3));
    }
  }
};

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    star(i, j, N);
  }
  result.push("\n");
}

console.log(result.join(""));
