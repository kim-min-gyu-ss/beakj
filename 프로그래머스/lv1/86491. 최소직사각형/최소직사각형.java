import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int mx = 0;
        int mn = 0;
        
        for (int[] size : sizes) {
            int tmpm = Math.max(size[0],size[1]);
            int tmpn = Math.min(size[0],size[1]);
            
            mx = Math.max(mx, tmpm);
            mn = Math.max(mn, tmpn);
        }
        
        return mx * mn;
    }
}