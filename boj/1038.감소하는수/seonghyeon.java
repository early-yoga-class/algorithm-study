import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static List<Long> decreaseNumbers = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=0;i<10;i++){
            countDecreaseNumber(i);
        }
        Collections.sort(decreaseNumbers);
        if(n > decreaseNumbers.size()) {
            System.out.println(-1);
        } else {
            System.out.println(decreaseNumbers.get(n));
        }
    }

    static void countDecreaseNumber(long n){
        decreaseNumbers.add(n);
        backtrack(n, n);
    }

    static void backtrack(long lastDigit, long currentNumber) {
        for(int nextDigit = 0; nextDigit < lastDigit; nextDigit++) {
            long newNumber = currentNumber * 10 + nextDigit;
            decreaseNumbers.add(newNumber);
            backtrack(nextDigit, newNumber);
        }
    }
}
