let fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

//import fs from "fs";
//const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const ts = input.shift();
const chars = ["+", "-", " "];

function permutation(arr, selectNum) {
  const result = [];
  if (selectNum === 1) return arr.map(v => [v]);

  arr.forEach((v, idx, arr) => {
    const fixed = v;
    const restArr = arr;
    const permutationArr = permutation(restArr, selectNum - 1);
    const combineFix = permutationArr.map(v => [fixed, ...v]);
    result.push(...combineFix);
  });
  return result;
}

for (let t = 0; t < ts; t++) {
  let ans = [];
  let ops = permutation(chars, +input.shift() - 1);
  for (const op of ops) {
    let n = 2;
    let str = "1";
    let print_str = "1";
    for (const ch of op) {
      if (ch === "+") {
        str += "+" + n;
        print_str += "+" + n;
      } else if (ch === "-") {
        str += "-" + n;
        print_str += "-" + n;
      } else {
        str += n;
        print_str += " " + n;
      }
      n++;
    }
    if (eval(str) === 0) {
      ans.push(print_str);
    }
  }

  ans.sort();
  for (const str of ans) {
    console.log(str);
  }
  console.log("");
}
