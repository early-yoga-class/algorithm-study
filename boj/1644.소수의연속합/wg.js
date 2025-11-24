const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim()

const N = parseInt(input)


function isPrime(num) {
  if (num < 2) return false;
  if (num === 2) return true;
  for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

let primes = [];
for (let i = 2; i <= N; i++) {
  if (isPrime(i)) primes.push(i);
}


let start = 0
let end = 1
let count = 0
let window = []
window.push(primes[start])
window.push(primes[end])

if (primes.includes(N)) {
  count += 1
}



while (start < end && end < primes.length - 1) {
  let sum = window.length > 0 ? window.reduce((prev, cur) => prev + cur) : 0
  if (sum < N) {
    end += 1
    window.push(primes[end])
  } else if (sum == N) {
    count += 1
    end += 1
    window.push(primes[end])
  } else {
    start += 1
    window.shift()
  }
}

console.log(count)