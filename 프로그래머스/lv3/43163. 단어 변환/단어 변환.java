import java.util.*;
class Solution {
    private int answer = 0;
    private List<String> already = new ArrayList<String>();
    
    public int solution(String begin, String target, String[] words) {
        dfs(begin,target,words,0);
        return answer;
    }
    
    private void dfs(String begin, String target, String[] words, int cnt) {
        
        if (begin.equals(target)) {
            answer = cnt;
            return;
        }
        
        if (already.contains(begin)) return;
        
        
        for (String str : words) {
            int tmp = 0;
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) != begin.charAt(i)) {
                    tmp++;
                }
            } 
            if (tmp == 1) {
                already.add(begin);
                // System.out.println(already);
                dfs(str, target, words, cnt+1);
            }
        }
    }
}