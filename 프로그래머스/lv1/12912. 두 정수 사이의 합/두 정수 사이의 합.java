class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if (a > b) {
            int tmp1 = b;
            int tmp2 = a;
            for (int i = tmp1; i <= tmp2; i++) {
            answer += i;
        }
        } else {
            int tmp1 = a;
            int tmp2 = b;
            for (int i = tmp1; i <= tmp2; i++) {
            answer += i;
        }
        }
        return answer;
    }
}