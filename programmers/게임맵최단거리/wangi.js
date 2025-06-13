function solution(maps) {
  var answer = 0;
  //     dx, dy 초기화
  let dx = [0, 0, 1, -1]
  let dy = [1, -1, 0, 0]

  //     Visited 기록용 초기화
  let M = maps.length; //  row
  let N = maps[0].length;// col
  let visited = Array.from({ length: M }, () => Array(N).fill(false))

  //     BFS
  function BFS(x, y, count) {
    let queue = [];
    queue.push([x, y, count]);
    visited[x][y] = true;

    while (queue.length != 0) {
      let [x, y, count] = queue.shift();

      if (x == M - 1 && y == N - 1) {
        answer = count;
        return;
      }

      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (0 <= nx && nx < M && 0 <= ny && ny < N) {
          if (!visited[nx][ny] && maps[nx][ny] != 0) {
            visited[nx][ny] = true;
            queue.push([nx, ny, ++count]);
          }
        }
      }
    }
  }

  BFS(0, 0, 1)

  return answer == 0 ? -1 : answer;
}