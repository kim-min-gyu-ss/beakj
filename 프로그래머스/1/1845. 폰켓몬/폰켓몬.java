import java.util.*;
class Solution {
    static HashSet<Integer> set = new HashSet<>();
    public int solution(int[] nums) {
        for (int num : nums) {
            set.add(num);
        }
        return (nums.length/2) > set.size() ? set.size() : nums.length/2;
    }
}