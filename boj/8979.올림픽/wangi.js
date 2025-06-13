const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

// 1. 입력 받기
let [N, K] = input[0].split(' ').map(Number);
console.log(N, K)
let medals = []
for (let i = 1; i <= N; i++) {
  let [num, gold, silver, bronze] = input[i].split(' ').map(Number);
  medals.push([num, gold, silver, bronze])
}
// console.log(medals)
// 2. 점수 계산 G : 100000, S : 100, B : 1
let score = []
medals.forEach((elem) => {
  [num, gold, silver, bronze] = elem
  let total = gold * 100000 + silver * 100 + bronze * 1
  score.push([num, total])
})

// 3. 점수로 정렬
score.sort((a, b) => b[1] - a[1])

// 4. K 국가 점수 찾기
let targetScore = 0;
for (let i = 0; i < score.length; i++) {
  if (score[i][0] === K) {
    targetScore = score[i][1];
    break;
  }
}

// 4. 배열에서 점수있는 idx 찾기
let rank = 0;
for (let i = 0; i < score.length; i++) {
  if (score[i][1] === targetScore) {
    rank = i + 1;
    break;
  }
}

console.log(rank)


