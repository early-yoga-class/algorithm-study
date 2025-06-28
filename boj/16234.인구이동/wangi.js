const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');


let [N, L, R] = input[0].split(' ').map(Number);

let graph = [];
for (let i = 1; i <= N; i++) {
  let row = input[i].split(' ').map(Number);
  graph.push(row);
}

let dx = [0, 0, -1, 1];
let dy = [-1, 1, 0, 0];

let answer = 0;

function BFS(x, y, visited) {
  let queue = [];
  queue.push([x, y]);
  visited[x][y] = true;

  let united = [[x, y]] // 연합 칸 저장용
  let count = 1; // 연합 칸 개수
  let population = graph[x][y]; // 연합 인구수 총합

  while (queue.length !== 0) {
    let [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      nx = x + dx[i];
      ny = y + dy[i];
      if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
        let diff = Math.abs(graph[x][y] - graph[nx][ny]);
        // 국경 열리는지 여부 판단
        if (L <= diff && diff <= R) {
          visited[nx][ny] = true;
          united.push([nx, ny])
          queue.push([nx, ny]);
          count += 1;
          population += graph[nx][ny];
        }
      }
    }
  }
  return { united, count, population }
}

while (true) {
  let ismoved = false;
  let visited = Array.from({ length: N }, () => Array(N).fill(false));
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j]) {
        let united_info = BFS(i, j, visited);

        if (united_info.count > 1) {
          ismoved = true; // 이동 발생 변경
          let new_population = Math.floor(united_info.population / united_info.count);
          for (let [x, y] of united_info.united) {
            graph[x][y] = new_population;
          }
        }
      }
    }
  }

  if (!ismoved) {
    break;
  }
  answer++;
}

console.log(answer);
