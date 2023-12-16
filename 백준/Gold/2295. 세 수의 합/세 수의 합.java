import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, idx, result, left, right;
    static int[] num, hap;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        num = new int[N];
        for (int i = 0; i < N; i++) {
            num[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(num);

        hap = new int[N * N];
        idx = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                hap[idx] = num[i] + num[j];
                idx++;
            }
        }
        Arrays.sort(hap);

        check:
        for (int i = N - 1; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                int gap = num[i] - num[j];
                if (isValid(gap)) {
                    result = num[i];
                    break check;
                }
            }
        }
        System.out.println(result);
    }
    private static boolean isValid(int goal) {
        int left = 0;
        int right = hap.length - 1;
        while(left <= right) {
            int mid = (left + right) / 2;
            if(goal == hap[mid]) {
                return true;
            } else if(goal > hap[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
