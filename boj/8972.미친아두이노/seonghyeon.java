import java.io.*;
import java.util.*;

public class BOJ {
    static int n, m;
    static int[][] board;
    static List<Arduino> arduinos = new ArrayList<>();
    static Arduino jongsu = null;
    static boolean gameOver = false;
    static int turn = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];

        // 종수 : -1, 빈칸 : 0, 미친 : 1
        for(int i = 0; i < n; i++){
            String line = br.readLine();
            for(int j = 0; j < m; j++){
                char c = line.charAt(j);
                if(c == 'I') {
                    board[i][j] = -1;
                    jongsu = new Arduino(i, j);
                } else if(c == 'R') {
                    board[i][j] = 1;
                    arduinos.add(new MadArduino(i, j));
                } else {
                    board[i][j] = 0;
                }
            }
        }

        String commands = br.readLine();

        for(char command : commands.toCharArray()){
            turn++;
            int direction = Character.getNumericValue(command) - 1;

            moveJongsu(direction);
            if(gameOver) {
                System.out.println("kraj " + turn);
                return;
            }

            moveMadArduinos();
            if(gameOver) {
                System.out.println("kraj " + turn);
                return;
            }

            handleCollisions();
        }

        printBoard();
    }

    private static void moveJongsu(int direction) {
        board[jongsu.x][jongsu.y] = 0;
        jongsu.move(direction);

        if(board[jongsu.x][jongsu.y] == 1) {
            gameOver = true;
            return;
        }
        board[jongsu.x][jongsu.y] = -1;
    }

    private static void moveMadArduinos() {
        for(Arduino arduino : arduinos) {
            if(arduino.isLive) {
                board[arduino.x][arduino.y] = 0;
            }
        }

        for(Arduino arduino : arduinos) {
            if(arduino.isLive) {
                ((MadArduino)arduino).findShortestPath(jongsu.x, jongsu.y);
            }
        }

        for(Arduino arduino : arduinos) {
            if(arduino.isLive && arduino.x == jongsu.x && arduino.y == jongsu.y) {
                gameOver = true;
                return;
            }
        }

        for(Arduino arduino : arduinos) {
            if(arduino.isLive) {
                board[arduino.x][arduino.y] = 1;
            }
        }
    }

    private static void handleCollisions() {
        Map<String, List<Arduino>> positionMap = new HashMap<>();

        for(Arduino arduino : arduinos) {
            if(arduino.isLive) {
                String key = arduino.x + "," + arduino.y;
                positionMap.computeIfAbsent(key, k -> new ArrayList<>()).add(arduino);
            }
        }

        for(List<Arduino> list : positionMap.values()) {
            if(list.size() >= 2) {
                for(Arduino arduino : list) {
                    arduino.isLive = false;
                    board[arduino.x][arduino.y] = 0;
                }
            }
        }
    }

    private static void printBoard() {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(board[i][j] == -1) {
                    sb.append('I');
                } else if(board[i][j] == 1) {
                    sb.append('R');
                } else {
                    sb.append('.');
                }
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }

    static class Arduino {
        int x, y;
        int[] dx = {1, 1, 1, 0, 0, 0, -1, -1, -1};
        int[] dy = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
        boolean isLive = true;

        Arduino(int i, int j) {
            x = i;
            y = j;
        }

        public void move(int idx) {
            if(!this.isLive) return;

            this.x += dx[idx];
            this.y += dy[idx];
        }
    }

    static class MadArduino extends Arduino {
        MadArduino(int i, int j) {
            super(i, j);
        }

        public void findShortestPath(int targetX, int targetY) {
            int minDistance = Integer.MAX_VALUE;
            int bestDirection = 4;

            for(int i = 0; i < 9; i++) {
                int nx = this.x + this.dx[i];
                int ny = this.y + this.dy[i];

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

                int manhattan = Math.abs(targetX - nx) + Math.abs(targetY - ny);
                if(manhattan < minDistance) {
                    minDistance = manhattan;
                    bestDirection = i;
                }
            }

            this.move(bestDirection);
        }
    }
}