import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int ln = nums.length;
        for (int i = 0; i < ln - 2; i++) {
            for (int j = i + 1; j < ln - 1; j++) {
                for (int k = j + 1; k < ln; k++) {
                    int hap = 0;
                    hap += nums[i] + nums[j] + nums[k];
                    answer += check(hap);
                }
            }
        }
        

        return answer;
    }
    private static int check(int hap) {
        for (int i = 2; i < Math.sqrt(hap) + 1; i++) {
            if (hap % i == 0) return 0;
        }
        return 1;
    }
}