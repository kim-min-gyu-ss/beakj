import java.util.*;
class Solution {
    public boolean solution(String s) { 
        if (s.length() != 4 && s.length() != 6) return false;
        
        for (int i = 0; i < s.length(); i++) {
            int tmp = s.charAt(i) - '0';
            if (tmp > 9) return false;
        }
        
        return true;
    }
}