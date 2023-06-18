import java.util.*;
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double sum = 0;
        int length = arr.length;
        for (int a : arr) {
            sum += a;
        }
        answer = (double)(sum/length);
        return answer;
    }
}