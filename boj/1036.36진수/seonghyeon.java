import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

public class Formation {

    static String[] thirtySix = {
            "0","1","2","3","4","5","6","7","8","9",
            "A","B","C","D","E","F","G","H","I","J","K","L",
            "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    };
    static Map<String, Integer> thirtySixFormation = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine().trim());

        for (int i = 0; i < 36; i++) {
            thirtySixFormation.put(thirtySix[i], i);
        }

        List<Number> numbers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<String> strings = Arrays.asList(bf.readLine().split(""));
            numbers.add(new Number(strings));
        }

        int k = Integer.parseInt(bf.readLine().trim());

        BigInteger[] delta = new BigInteger[36];
        Arrays.fill(delta, BigInteger.ZERO);

        BigInteger originalSum = BigInteger.ZERO;

        for (Number num : numbers) {
            originalSum = originalSum.add(num.decimal);
            calcDelta(num, delta);
        }

        List<BigInteger> deltaList = Arrays.asList(delta);
        deltaList.sort((a, b) -> b.compareTo(a));

        BigInteger add = BigInteger.ZERO;
        for (int i = 0; i < k; i++) {
            add = add.add(deltaList.get(i));
        }

        BigInteger result = originalSum.add(add);

        System.out.println(toBase36(result));
    }

    private static void calcDelta(Number num, BigInteger[] delta) {
        int len = num.numbers.size();

        BigInteger base = BigInteger.ONE;

        for (int i = len - 1; i >= 0; i--) {
            int value = thirtySixFormation.get(num.numbers.get(i));

            int diff = 35 - value;
            if (diff > 0) {
                delta[value] = delta[value].add(base.multiply(BigInteger.valueOf(diff)));
            }

            base = base.multiply(BigInteger.valueOf(36));
        }
    }

    private static String toBase36(BigInteger number) {
        if (number.equals(BigInteger.ZERO)) return "0";

        StringBuilder sb = new StringBuilder();

        BigInteger base = BigInteger.valueOf(36);

        while (number.compareTo(BigInteger.ZERO) > 0) {
            BigInteger[] qr = number.divideAndRemainder(base);
            int idx = qr[1].intValue();
            sb.append(thirtySix[idx]);
            number = qr[0];
        }

        return sb.reverse().toString();
    }

    static class Number {
        BigInteger decimal;
        List<String> numbers;

        public Number(List<String> numbers) {
            this.numbers = numbers;
            thirtySixToDecimal();
        }

        private void thirtySixToDecimal() {
            BigInteger base = BigInteger.ONE;
            BigInteger sum = BigInteger.ZERO;

            for (int i = numbers.size() - 1; i >= 0; i--) {
                int value = thirtySixFormation.get(numbers.get(i));
                sum = sum.add(base.multiply(BigInteger.valueOf(value)));
                base = base.multiply(BigInteger.valueOf(36));
            }

            this.decimal = sum;
        }
    }
}