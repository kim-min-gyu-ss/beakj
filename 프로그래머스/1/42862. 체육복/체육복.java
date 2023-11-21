import java.util.*;
class Solution {
    static HashSet<Integer> set = new HashSet<>();
    static HashSet<Integer> give = new HashSet<>();
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        int result = 0;
        for (int ls : lost) {
            set.add(ls);
        }
        for (int rev : reserve) {
            if (set.contains(rev)) {
                set.remove(rev);
                result++;
            } else {
                give.add(rev);
            }
        }
        for (Integer g : give) {
            if (set.contains(g - 1)) {
                set.remove(g - 1);
                result++;
            } else if (set.contains(g + 1)) {
                set.remove(g + 1);
                result++;
            }
        }
        
        return answer + result;
    }
}