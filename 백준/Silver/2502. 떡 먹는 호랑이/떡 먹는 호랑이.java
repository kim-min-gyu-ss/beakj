import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int D, K;
    static int[] dp;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        D = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        dp = new int[D];
        dp[D - 1] = K;

        int cnt = 1;
        check:
        while(true) {
            dp[0] = cnt;
            for (int i = cnt; i < K; i++) {
                dp[1] = i;
                for (int j = 2; j < D - 1; j++) {
                    dp[j] = dp[j - 1] + dp[j - 2];
                }
                if (K == dp[D - 2] + dp[D - 3]) {
                    System.out.println(dp[0]);
                    System.out.println(dp[1]);
                    break check;
                }
            }
            cnt++;
        }
    }
}
