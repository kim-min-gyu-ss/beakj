class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long tmp = 0;
        int cnt = 1;
        for (int i = 0; i < count; i ++) {
            tmp += cnt * price;    
            cnt ++;
        }
        if (tmp > money) {
            answer = tmp - money;
            return answer;
        }
        answer = 0;
        return answer;
    }
}