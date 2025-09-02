const dx = [0, -1, 0];
const dy = [-1, 0, 1];

const main = (n, m, d, gr) => {

  // 3명 궁수 조합 생성
  const combinations = [];
  const makeCombination = (arr, idx) => {
    if (arr.length === 3) {
      combinations.push(arr);
      return;
    }
    for (let i = idx + 1; i < m; i++) {
      makeCombination([...arr, i], i);
    }
  };
  makeCombination([], -1);
  let answer = 0;

  for (const combi of combinations) {
    const game = gr.map((v) => [...v]);

    let enemy = 0;
    // Stage 진행
    for (let stage = 0; stage < n; stage++) {
      const v = new Set();
      for (let y of combi) {
        const q = [[n - 1, y, 1]];
        while (q.length) {
          const [cx, cy, cnt] = q.shift();
          if (game[cx][cy] === 1) {
            v.add(cx * m + cy);
            break;
          }
          if (cnt >= d) continue;
          // BFS로 몬스터 검사
          for (let i = 0; i < 3; i++) {
            const nx = cx + dx[i];
            const ny = cy + dy[i];
            if (nx < 0 || ny < 0 || ny >= m) continue;
            q.push([nx, ny, cnt + 1]);
          }
        }
      }
      for (const value of v) {
        const nn = Math.floor(value / m);
        const mm = value % m;
        game[nn][mm] = 0;
      }
      enemy += v.size;
      const pushArray = Array.from({ length: m }, () => 0);
      game.pop();
      game.unshift(pushArray);
    }
    answer = Math.max(answer, enemy);
  }
  console.log(answer);
};
const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

const [n, m, d] = input[0].split(' ').map((v) => +v);
const gr = input.slice(1).map((v) => v.split(' ').map((v) => +v));
main(n, m, d, gr);