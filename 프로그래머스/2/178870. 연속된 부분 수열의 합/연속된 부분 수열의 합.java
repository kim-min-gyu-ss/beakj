class Solution {
    static int[] answer;
    static int left, right, hap, leng;
    public int[] solution(int[] sequence, int k) {
        leng = sequence.length;
        answer = new int[] {0, leng - 1};
        left = 0;
        right = 1;
        hap = sequence[0];
        while (left < right) {
            if (hap == k) {
                moveIdx();
                hap -= sequence[left++];
            } else if (hap > k) {
                hap -= sequence[left++];
            } else if (right < leng) {
                hap += sequence[right++];
            } else break;
        }
        return answer;
    }
    private void moveIdx() {
            if (right - left - 1 < answer[1] - answer[0]) {
                answer[0] = left;
                answer[1] = right - 1;
            }
        }
}