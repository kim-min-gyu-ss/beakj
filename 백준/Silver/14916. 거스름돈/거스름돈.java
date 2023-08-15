import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

    static int[] dp;

    public static void main(String[] args) throws IOException {

        dp = new int[100001];
        dp[0] = -1;
        dp[1] = -1;
        dp[2] = 1;
        dp[3] = -1;
        dp[4] = 2;
        dp[5] = 1;

        for (int i = 6; i < 100001; i++) {
            if (dp[i - 5] != -1) {
                dp[i] = dp[i - 5] + 1;
            } else if (dp[i - 2] != -1) {
                dp[i] = dp[i - 2] + 1;
            } else {
                dp[i] = -1;
            }
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int idx = Integer.parseInt(st.nextToken());
        System.out.print(dp[idx]);
    }
}