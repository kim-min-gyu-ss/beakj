import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        HashSet<String> list = new HashSet<String>();
        int cnt = 0;
        list.add(words[0]);
        String word = words[0];
        
        for (int i = 1; i < words.length; i++) {
            if (list.contains(words[i])) {
                return result(n,i);
            } else {
                if (word.charAt(word.length() - 1) != words[i].charAt(0)) {
                    return result(n,i);
                }
                word = words[i];
                cnt++;
                list.add(words[i]);
            }
        }
        return new int[] {0,0};
    }
    
    private static int[] result(int n, int m) {
        int cnt = (m/n) + 1;
        int round = (m%n) + 1;
        return new int[] {round, cnt};
    }
        
}