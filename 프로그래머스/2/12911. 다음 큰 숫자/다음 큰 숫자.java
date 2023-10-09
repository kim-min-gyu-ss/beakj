class Solution {
    public int solution(int n) {
        int answer = 0;
        int count = check(n);
        int index = 1;
        while (true) {
            int number = n + index;
            if (count == check(number)) {
                answer = number;
                break;
            }
            index++;
        }
        return answer;
    }

    public int check(int x) {
        String str = Integer.toBinaryString(x);
        int count = 0;
        char[] strArr = str.toCharArray();
        for (char val : strArr) {
            if (val == '1') count++;
        }
        return count;
    }
}