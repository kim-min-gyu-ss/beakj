class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 1;
        int tmp = m;
        int idx = section[0];
        for (int num : section) {
            if (tmp + idx - num <= 0) {
                answer++;
                tmp = m;
                idx = num;
                
            }
            tmp = tmp + idx - num ;
            idx = num;
        }
        return answer;
    }
}