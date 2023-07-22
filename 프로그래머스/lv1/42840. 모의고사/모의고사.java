import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] supo1 = {1,2,3,4,5};
        int[] supo2 = {2,1,2,3,2,4,2,5};
        int[] supo3 = {3,3,1,1,2,2,4,4,5,5};
        
        int[] tmp = {0,0,0};
        int cnt = 0;
        
        int ln1 = supo1.length;
        int ln2 = supo2.length;
        int ln3 = supo3.length;
        
        for (int i : answers) {
            if (i == supo1[cnt%ln1]) {
                tmp[0] += 1;
            }
            
            if (i == supo2[cnt%ln2]) {
                tmp[1] += 1;
            }
            
            if (i == supo3[cnt%ln3]) {
                tmp[2] += 1;
            }
            cnt++;
        }
        
        int max = -1;
        for (int i = 0; i < 3; i++) {
            if (max < tmp[i]) {
                max = tmp[i];
            }
        }
        
        int rst_cnt = 0;
        for (int i = 0; i < 3; i++) {
            if (max == tmp[i]) {
                rst_cnt++;
            }
        }
        
        int[] answer = new int[rst_cnt];
        int idx = 0;
        for (int i = 0; i < 3; i++) {
            if (max == tmp[i]) {
                answer[idx] = i+1;
                idx++;
            }
        }
        
        return answer;
    }
}