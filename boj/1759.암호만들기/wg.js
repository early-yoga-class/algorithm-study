const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

const [L, C] = input[0].split(' ').map(Number);
const alphabets = input[1].split(' ').sort();

const vowels = ['a', 'e', 'i', 'o', 'u']

// 백트래킹?
let result = []
let stack = []

const dfs = (start, vowelCnt, consonantCnt) => {
  if (stack.length == L) {
    if (vowelCnt >= 1 && consonantCnt >= 2) {
      result.push(stack.join(''))
    }
    return;
  }

  const need = L - stack.length

  for (let i = start; i <= alphabets.length - need; i++) {
    let char = alphabets[i]

    stack.push(char)

    if (vowels.includes(char)) {
      dfs(i + 1, vowelCnt + 1, consonantCnt)
    } else {
      dfs(i + 1, vowelCnt, consonantCnt + 1)
    }

    stack.pop()
  }
}


dfs(0, 0, 0)

console.log(result.join('\n'))
