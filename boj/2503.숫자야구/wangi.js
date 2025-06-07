const [N, ...nums] = require('fs').readFileSync('input.txt').toString().trim().split('\n');
let res = [];

for (let i = 0; i < Number(N); i++) {
  findBaseBallCnt(nums[i]);
}
console.log(res.length);  // 결과 출력

function findBaseBallCnt(numInfo) {
  const [number, strike, ball] = numInfo.split(' ').map(Number);
  const resNumArr = [];

  // 1~ 9, Brute Force 진행
  for (let i = 1; i < 10; i++) {
    for (let j = 1; j < 10; j++) {
      for (let k = 1; k < 10; k++) {
        // 111, 323 과 같이 숫자가 같은 경우를 제외
        if (i === j || j === k || k === i) continue;

        const curr = String(i) + String(j) + String(k);
        const count = { strike: 0, ball: 0 };

        for (let l = 0; l < String(number).length; l++) {
          // input으로 받은 수와 현재 조합된 curr에서 겹치는 수의 인덱스
          const idx = curr.indexOf(number.toString()[l]);

          // 인덱스가 반복문 변수 l과 같을 때 숫자와 자리가 모두 같은 strike이며
          // -1이 아닌 경우 숫자는 일치하지만 자리가 다를 경우인 ball에 해당함
          if (idx === l) count.strike += 1;
          else if (idx !== -1) count.ball += 1;
        }

        if (strike === count.strike && ball === count.ball) resNumArr.push(curr);
      }
    }
  }
  // res에서 중복된 요소만 담기
  if (res.length === 0) res = [...resNumArr];
  else res = resNumArr.filter(ele => res.includes(ele));
}