class Solution {
    public long solution(long n) {
        long answer = 0;
        for (long i = 1; i < n+1; i++) {
            if (i*i == n) {
                answer = (i+1) * (i+1);
                break;
            }
        }
        
        return answer == 0 ? -1 : answer;
    }
}