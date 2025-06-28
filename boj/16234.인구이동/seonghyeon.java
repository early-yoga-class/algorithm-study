import java.util.*;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {

    static int n,l,r;
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};
    static int[][] A;
    static Queue<Cord> queue = new LinkedList<>();
    static Queue<Union> unions = new LinkedList<>();
    static boolean[][] visited;

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        A = new int[n][n];


        for(int i=0;i<n;i++){
            st=new StringTokenizer(bf.readLine());
            for(int j=0;j<n;j++){
                A[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        int result = 0;
        do{
            visited = new boolean[n][n];
            unions.clear();
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    if(!visited[i][j]){
                        Optional<Union> bfs = Bfs(i, j);
                        bfs.ifPresent(union -> unions.add(union));
                    }
                }
            }

            for (Union union : unions) {
                union.move();
            }
            result++;
        }while(!unions.isEmpty());


        System.out.println(--result);
    }

    private static Optional<Union> Bfs(int x, int y){
        visited[x][y]=true;
        queue.add(new Cord(x,y));
        Union union = new Union();

        while(!queue.isEmpty()){
            Cord cord = queue.poll();
            union.addNation(cord);
            for(int i=0;i<4;i++){
                int nx = cord.x+dx[i];
                int ny = cord.y+dy[i];

                if((0<=nx && nx<n && 0<=ny && ny<n)){
                    int diff = Math.abs(A[cord.x][cord.y] - A[nx][ny]);
                    if(!visited[nx][ny] && (l<=diff && diff<=r)){
                        visited[nx][ny] = true;
                        queue.add(new Cord(nx,ny));
                    }
                }
            }
        }
        if(union.getSize() == 1){
            union = null;
        }

        return Optional.ofNullable(union);
    }
    static class Union{
        int size;
        int people;

        Queue<Cord> nations = new LinkedList<>();

        public Union(){
            this.people=0;
            this.size=0;
        }

        public int getSize(){
            return size;
        }

        public void addNation(Cord cord){
            nations.add(cord);
            size++;
            people+=A[cord.x][cord.y];
        }

        private int calculatePeople(){
            return people/size;
        }

        public void move(){
            int avg = calculatePeople();
            while(! nations.isEmpty()){
                Cord poll = nations.poll();

                A[poll.x][poll.y] = avg;
            }
        }
    }

    static class Cord{
        int x;
        int y;

        public Cord(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
}