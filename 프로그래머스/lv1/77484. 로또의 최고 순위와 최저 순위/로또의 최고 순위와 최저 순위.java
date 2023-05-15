import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer;
        List<Integer> result = new ArrayList<Integer>();
        int temp = 0;
        int zero = 0;
        for (int a : lottos) {
            if (a == 0) {
                zero++;
                continue;
                }
            for (int b : win_nums) {
                if (a == b) {
                    temp++;
                    }
                }
            }
        int temp2 = temp + zero;
        if (temp == 0) {temp = 1;}
        if (temp2 == 0) {temp2 = 1;}
        if (temp2 > 6) {temp2 = 6;}
        answer = new int[2];
        answer[0] = 7 - temp2;
        answer[1] = 7 - temp;
        return answer;
    }
}