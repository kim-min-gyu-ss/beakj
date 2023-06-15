import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int leng = commands.length;
        for (int i = 0; i < leng; i++) {
            int[] temp = new int[commands[i][1] - commands[i][0] + 1];
            for (int j = 0; j <= commands[i][1] - commands[i][0]; j++) {
                temp[j] = array[j + commands[i][0] - 1];
            }
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2] - 1];
        }
        return answer;
    }
}