let fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let S = input[0].split("");

let cnt = S.length;

let zero = 0;
for (let i = 0; i < cnt; i++) {
  if (S[i] == "0") {
    zero++;
  }
}

let one_cnt = Math.floor((cnt - zero) / 2);
let zero_cnt = Math.floor(zero / 2);

for (let i = 0; i < cnt && one_cnt != 0; i++) {
  if (S[i] === "1") {
    S[i] = "2";
    one_cnt--;
  }
}

for (let i = cnt - 1; i >= 0 && zero_cnt != 0; i--) {
  if (S[i] === "0") {
    S[i] = "2";
    zero_cnt--;
  }
}

console.log(S.filter(ch => ch !== "2").join(""));
