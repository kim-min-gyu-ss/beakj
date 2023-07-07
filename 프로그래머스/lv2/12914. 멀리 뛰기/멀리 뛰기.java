class Solution {
    public long solution(int n) {
        long answer = 0;
        int[] dp = new int[n+1];
        if (n == 1) return 1;
        if (n == 2) return 2;
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        for (int i = 4; i < n+1; i++) {
            dp[i] = (dp[i-2] + dp[i-1]) %1234567;
        }
        answer = dp[n];
        return answer;
    }
}