import java.util.Scanner;

public class Rain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        int result = 0;

        int[] heights = new int[w];

        for(int i=0;i<w;i++) heights[i] = sc.nextInt();

        int[] left = new int[w];
        int[] right = new int[w];
        int maxHeight = 0;
        for(int i=0;i<w;i++){
            maxHeight = Math.max(maxHeight, heights[i]);
            left[i]=maxHeight;
        }

        maxHeight = 0;
        for(int i=w-1;i>=0;i--){
            maxHeight = Math.max(maxHeight, heights[i]);
            right[i] = maxHeight;
        }

        for(int i=0;i<w;i++){
            int min = Math.min(right[i], left[i]);
            if(min>heights[i]) {
                result += min - heights[i];
            }
        }

        System.out.println(result);
    }
}
