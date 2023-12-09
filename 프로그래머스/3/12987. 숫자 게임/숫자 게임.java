import java.util.*;
class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        int leng = A.length;
        Arrays.sort(A);
        Arrays.sort(B);
        int idx = 0;
        for (int i = 0; i < leng; i++) {
            check:
            for (int j = idx; j < leng; j++) {
                if (A[i] < B[j]) {
                    idx = j + 1;
                    answer++;
                    break check;
                }
            }
        }
        return answer;
    }
}