import java.util.*;
class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String tmp = Integer.toString(x);
        int hap = 0;
        for (int i = 0; i < tmp.length(); i++) {
            hap += tmp.charAt(i) - '0';
        }
        return (x % hap) == 0 ? true : false;
    }
}