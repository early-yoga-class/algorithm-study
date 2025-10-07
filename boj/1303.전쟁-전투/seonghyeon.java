import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int n,m,w,b;
    static boolean[][] visited;
    static String[][] cloths;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        w=0;
        b=0;
        cloths = new String[m][n];
        visited = new boolean[m][n];

        for(int i=0;i<m;i++){
            String[] temp = sc.next().split("");
            for(int j=0;j<n;j++){
                cloths[i][j] = temp[j];
            }
        }

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(!visited[i][j]){
                    bfs(i,j);
                }
            }
        }

        System.out.println(w+" "+b);
    }

    static void bfs(int x, int y){
        String nowColor = cloths[x][y];
        Queue<Cord> queue = new LinkedList<>();
        queue.add(new Cord(x,y));
        visited[x][y] = true;
        int count = 0;

        while(!queue.isEmpty()){
            Cord cord = queue.poll();
            count++;

            for(int i=0;i<4;i++){
                int nx = cord.x+dx[i];
                int ny = cord.y+dy[i];

                if(nx>=0 && nx<m && ny>=0 && ny<n){
                    if(!visited[nx][ny] && cloths[nx][ny].equals(nowColor)){
                        visited[nx][ny] = true;
                        queue.add(new Cord(nx,ny));
                    }
                }
            }
        }

        if(nowColor.equals("W")){
            w+=(count*count);
        }else{
            b+=(count*count);
        }
    }

    static class Cord{
        int x;
        int y;

        Cord(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
