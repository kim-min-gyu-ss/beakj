class Solution {
    public int solution(int[] number) {
        int answer = 0;
        int leng = number.length;
        int tmp = 0;
        for (int i = 0; i < leng - 2; i++) {
            tmp += number[i];
            for (int j = i + 1; j < leng - 1; j++) {
                tmp += number[j];
                for (int k = j + 1; k < leng; k ++) {
                    tmp += number[k];
                    if (tmp == 0) {
                        answer++;
                    }
                    tmp -= number[k];
                }
                tmp -= number[j];
            }
            tmp -= number[i];
        }
        return answer;
    }
}