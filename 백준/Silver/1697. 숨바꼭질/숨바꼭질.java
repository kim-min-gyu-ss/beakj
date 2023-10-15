import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int start, end;
    static int[] dp;
    static Queue<Integer> q = new LinkedList<>();
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());
        dp = new int[100001];
        System.out.println(bfs(start));
    }

    private static int bfs(int now) {
        q.add(now);
        dp[now] = 1;
        while (!q.isEmpty()) {
            int n = q.poll();
            if (n == end) return dp[n] - 1;
            if (n - 1 >= 0 && dp[n - 1] == 0) {
                dp[n - 1] = dp[n] + 1;
                q.add(n - 1);
            }
            if (n + 1 <= 100000 && dp[n + 1] == 0) {
                dp[n + 1] = dp[n] + 1;
                q.add(n + 1);
            }
            if (2 * n <= 100000 && dp[2 * n] == 0) {
                dp[2 * n] = dp[n] + 1;
                q.add(2 * n);
            }
        }
        return -1;
    }
}

