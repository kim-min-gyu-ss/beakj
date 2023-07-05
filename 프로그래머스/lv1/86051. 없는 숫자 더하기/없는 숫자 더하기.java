class Solution {
    public int solution(int[] numbers) {
        int answer = -1;
        int tmp = 45;
        for (int i : numbers) {
            tmp -= i;
        }
        answer = tmp;
        return answer;
    }
}