import java.util.*;

class Solution {
    static Set<Integer> ans = new HashSet<>();
    static int leng;
    public static int solution(int[] elements) {
        leng = elements.length;
        for (int i = 1; i <= leng; i++) {
            for (int j = 0; j < leng; j++) {
                int sum = 0;
                for (int k = 0; k < i; k++) {
                    sum += (j + k > leng - 1) 
                        ? elements[j + k - leng] 
                        : elements[j + k];

                }
                if (sum != 0) ans.add(sum);
            }
        }
        return ans.size();
    }
}