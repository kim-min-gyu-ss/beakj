import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = check(n);
        return answer;
    }

    private static int check(int n) {
        if (n < 2) return 0;
        int result = 0;
        for (int i = 2; i < n + 1; i++) {
            if (isPrime(i)) {
                result++;
            }
        }
        return result;
    }

    private static boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
