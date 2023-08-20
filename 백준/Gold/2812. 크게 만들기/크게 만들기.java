import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int K;
    static String str;

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        str = br.readLine();
        Stack<Integer> stack = new Stack<>();

        int cnt = 0;
        for (int i = 0; i < str.length(); i++) {
            int tmp = str.charAt(i) - '0';
            while(cnt < K && !stack.isEmpty() && stack.peek() < tmp) {
                cnt++;
                stack.pop();
            }
            stack.add(tmp);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N - K; i++) {
            sb.append(stack.get(i));
        }
        System.out.println(sb);
    }
}