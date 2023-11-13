import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        if (s < n) return new int[]{-1}; 

        int dv = s / n;
        int rm = s % n;

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = dv;
        }

        int cnt=0;
        while(rm > 0){
            // if(cnt >= n) idx=0;
            cnt++;
            answer[cnt]++;
            rm--;
        }

        Arrays.sort(answer);


        return answer;
    }
}