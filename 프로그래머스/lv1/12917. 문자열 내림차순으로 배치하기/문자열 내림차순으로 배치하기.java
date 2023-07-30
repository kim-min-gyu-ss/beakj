import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        // char[] tmp = new String[s.length()];
        char[] tmp = s.toCharArray();
        System.out.println(tmp);
        Arrays.sort(tmp);
        System.out.println(tmp);
        for (int i = tmp.length - 1; i > -1; i--) {
            answer += Character.toString(tmp[i]);
        }
        return answer;
    }
}