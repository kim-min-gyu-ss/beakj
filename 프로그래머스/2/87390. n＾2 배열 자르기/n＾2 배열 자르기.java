class Solution {
    static int[] arrs;
    public int[] solution(int n, long left, long right) {
        int[] arrs = new int[(int)(right - left) + 1];
        for (int i = 0; i < arrs.length; i++) {
            int y = (int)(left / n + 1);
            int x = (int)(left % n + 1);
            left++;
            arrs[i] = Math.max(y, x);
        }
        return arrs;
    }
}