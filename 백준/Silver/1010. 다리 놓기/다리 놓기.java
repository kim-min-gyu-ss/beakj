import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] dp = new int[31][31];
    static int T;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++)
        {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            System.out.println(combination(M, N));
        }
    }
    public static int combination(int n, int r)
    {

        if (dp[n][r] > 0)
        {
            return dp[n][r];
        }

        else if (n == r || r == 0)
        {
            return dp[n][r] = 1;
        }

        else
        {
            return dp[n][r] = combination(n - 1, r - 1) + combination(n - 1, r);
        }
    }
}