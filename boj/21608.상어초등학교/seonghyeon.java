import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Main {
    static int[][] board;

    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        board = new int[n+1][n+1];
        int[][] myFriend = new int[n*n + 1][4];

        for(int p=1;p<=n*n;p++) {
            int studentNo = sc.nextInt();
            for(int k=0;k<4;k++) {
                int temp = sc.nextInt();
                myFriend[studentNo][k] = temp;
            }

            List<int[]> cords = nominatedCordByRule1(myFriend[studentNo]);
            int[] cord = cords.get(0);

            if(cords.size() > 1) {
                cord = nominatedCordByRule2(cords);
            }
            board[cord[0]][cord[1]] = studentNo;
        }

        int result = calculateFriendShip(n, myFriend);
        System.out.println(result);
    }

    private static List<int[]> nominatedCordByRule1(int[] myFriend){
        int maxCnt = -1;
        List<int[]> result = new ArrayList<>();
        for(int i=1;i<=n;i++) {

            for(int j=1;j<=n;j++) {
                if(board[i][j] != 0) continue;
                int cnt = 0;

                for(int k=0;k<4;k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];

                    if(nx>=1&&nx<=n&&ny>=1&&ny<=n) {
                        for(int idx=0;idx<4;idx++) {
                            if(board[nx][ny] == myFriend[idx]) {
                                cnt++;
                                break;
                            }
                        }
                    }
                }
                if(maxCnt < cnt) {
                    result.clear();
                    result.add(new int[] {i, j});
                    maxCnt = cnt;
                }else if(maxCnt == cnt) {
                    result.add(new int[] {i,j});
                }
            }

        }
        return result;
    }

    private static int[] nominatedCordByRule2(List<int[]> cords){
        int maxCnt = -1;
        int[] result = cords.get(0);
        for(int[] cord : cords) {
            int cnt=0;
            for(int i=0;i<4;i++) {
                int nx = cord[0] + dx[i];
                int ny = cord[1] + dy[i];

                if(nx>=1&&nx<=n&&ny>=1&&ny<=n && board[nx][ny]==0) cnt++;
            }
            if(maxCnt < cnt) {
                result = cord;
                maxCnt = cnt;
            }
        }
        return result;
    }
    private static int calculateFriendShip(int n, int[][] myFriend) {
        int result = 0;
        for(int i=1;i<=n;i++) {
            for(int j=1;j<=n;j++) {
                int count = 0;
                for(int k=0;k<4;k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    for(int idx=0;idx<4;idx++) {
                        if(nx>=1&&nx<=n&&ny>=1&&ny<=n) {
                            if(board[nx][ny]==myFriend[board[i][j]][idx]) {
                                count++;
                            }
                        }
                    }
                }
                if(count == 4) result+=1000;
                else if(count == 3) result += 100;
                else if(count == 2) result += 10;
                else if(count == 1) result += 1;
            }
        }
        return result;
    }
}
