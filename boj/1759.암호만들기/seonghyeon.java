import java.util.*;

public class Main {
    static int L,C;
    static List<String> result = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        List<String> alphabet = new ArrayList<>();

        L = sc.nextInt();
        C = sc.nextInt();

        for (int i=0;i<C;i++) {
            String s = sc.next();
            alphabet.add(s);
        }
        Collections.sort(alphabet);


        Set<String> used = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        dfs(0, alphabet, used,sb,0);

        for(String s : result){
            System.out.println(s);
        }
    }

    static void dfs(int depth, List<String> alphabet, Set<String> used, StringBuilder word, int start){
        if(depth==L){
            int count = findGather(word.toString());
            if(count >= 1 && L-count >= 2){
                result.add(word.toString());
            }
        }

        for (int i = start; i<alphabet.size();i++){
            String s = alphabet.get(i);
            if(!used.contains(s)){
                used.add(s);
                word.append(s);
                dfs(depth+1, alphabet, used, word, i);
                word.deleteCharAt(word.length()-1);
                used.remove(s);
            }
        }
    }

    static int findGather(String word){
        String[] temp = word.split("");

        int cnt = 0;
        for (String s : temp){
            if(s.matches(".*[aeiou].*")){
                cnt++;
            }
        }
        return cnt;
    }
}
