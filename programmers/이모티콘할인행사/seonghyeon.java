class Solution {
    int[] discounts = {10, 20, 30, 40};
    Emoticon[] emo;
    int maxSubscriber = 0;
    int maxSales = 0;

    public int[] solution(int[][] users, int[] emoticons) {
        emo = new Emoticon[emoticons.length];
        int i = 0;
        for (int price : emoticons) {
            emo[i] = new Emoticon(i, price);
            i++;
        }

        dfs(0, users);

        return new int[]{maxSubscriber, maxSales};
    }

    private void dfs(int idx, int[][] users) {
        if (idx == emo.length) {
            evaluate(users);
            return;
        }

        for (int d = 0; d < discounts.length; d++) {
            emo[idx].setDiscountIdx(d);
            dfs(idx + 1, users);
        }
    }

    private void evaluate(int[][] users) {
        int subscriber = 0;
        int sales = 0;

        for (int[] user : users) {
            int minDiscount = user[0];
            int limit = user[1];
            int total = 0;

            for (Emoticon e : emo) {
                int appliedDiscount = discounts[e.discountIdx];
                if (appliedDiscount >= minDiscount) {
                    total += e.calculateDiscountPrice(discounts);
                }
            }

            if (total >= limit) {
                subscriber++;
            } else {
                sales += total;
            }
        }

        if (subscriber > maxSubscriber) {
            maxSubscriber = subscriber;
            maxSales = sales;
        } else if (subscriber == maxSubscriber && sales > maxSales) {
            maxSales = sales;
        }
    }

    private class Emoticon {
        int price;
        int number;
        int discountIdx;

        Emoticon(int num, int value) {
            this.number = num;
            this.price = value;
            this.discountIdx = 0;
        }

        void setDiscountIdx(int x) {
            this.discountIdx = x;
        }

        int calculateDiscountPrice(int[] discounts) {
            int d = discounts[this.discountIdx];
            return this.price * (100 - d) / 100;
        }
    }
}