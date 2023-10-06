import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        int stack = 0;
        for (int i = 0; i < s.length(); i++) {
            if (stack == 0) {
                answer += String.valueOf(s.charAt(i)).toUpperCase();
            } else {
                answer += String.valueOf(s.charAt(i)).toLowerCase();
            }
            stack++;
            if (s.charAt(i) == ' ') {
                stack = 0;
            }
        }
        return answer;
    }
}