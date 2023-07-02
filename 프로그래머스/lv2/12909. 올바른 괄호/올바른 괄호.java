import java.util.*;

class Solution {
    boolean solution(String s) {
        int tmp = 0;
        int leng = s.length();
        for (int i =0; i < leng; i ++) {
            if (s.charAt(i) == '(') {
                tmp ++;
            }
            if (s.charAt(i) == ')') {
                if (tmp > 0) {
                    tmp --;    
                } else{
                    return false;
                }
            }
        }
        if (tmp == 0) {
            return true;
        } else {
            return false;
        }
    }
}