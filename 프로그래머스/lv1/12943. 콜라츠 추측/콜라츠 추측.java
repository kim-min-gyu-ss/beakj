class Solution {
    public int solution(int num) {
        if (num == 1) {
            return 0;
        } else {
            int tmp = 1;
            while(tmp < 500) {
                if (num % 2 == 1) {
                    num = num * 3 + 1;
                } else {
                    num = num / 2;
                }
                if (num == 1) break;
                tmp++;
            }
            return tmp==500 ? -1 : tmp;    
        }
        
    }
}