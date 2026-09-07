import java.io.*;
import java.util.*;

class Solution {

    static long[] getPoint(int[] l1, int[] l2){
        long A = l1[0];
        long B = l1[1];
        long E = l1[2];
        long C = l2[0];
        long D = l2[1];
        long F = l2[2];
        long div = A*D - B*C;
        
        if (div == 0) return null;
        
        long xTop = B*F - E*D;
        long yTop = E*C - A*F;
        
        if (xTop % div !=0 || yTop%div !=0) return null;
        
        long x = xTop/div;
        long y = yTop/div;
        return new long[]{x, y};
    }
        
        
    public String[] solution(int[][] line) {
        List<long[]> points = new ArrayList<>();
            
        for (int i = 0; i<line.length; i++){
            for (int j = i+1; j<line.length; j++){
                long[] point = getPoint(line[i], line[j]);
                if (point != null) points.add(point);
            }
        }

        long minX = Long.MAX_VALUE;
        long maxX = Long.MIN_VALUE;
        long minY = Long.MAX_VALUE;
        long maxY = Long.MIN_VALUE;

        for (long[] p : points){
            minX = Math.min(minX, p[0]);
            maxX = Math.max(maxX, p[0]);
            minY = Math.min(minY, p[1]);
            maxY = Math.max(maxY, p[1]);
        }

        int width = (int) (maxX - minX + 1);
        int height = (int) (maxY - minY + 1);

        char[][] board = new char[height][width];

        for (int i = 0; i< height; i++){
            Arrays.fill(board[i], '.');
        }

        for (long[] p : points){
            int x = (int) (p[0] - minX);
            int y = (int) (maxY - p[1]);
            board[y][x] = '*';
        }
        
        String[] answer = new String[height];
        
        for (int i = 0; i < height; i++) {
            answer[i] = new String(board[i]);
        }

        return answer;
            
    }

}