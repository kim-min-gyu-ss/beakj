import java.util.*;
class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int leng = arr1.length;
        int leng2 = arr1[0].length;
        int[][] answer = new int[leng][leng2];
        for (int i = 0; i < leng; i++) {
            for (int j = 0; j < leng2; j++) {
                answer[i][j] += arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }
}