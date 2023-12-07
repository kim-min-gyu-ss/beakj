import java.io.*;
import java.util.*;

public class Main {
    static int N, cnt, idx;
    static int[] num;
    static Stack<Integer> stack = new Stack<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        num = new int[N];
        cnt = 1;
        idx = 0;
        for (int i = 0; i < N; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }
        while (idx < N) {
            if (num[idx] == cnt) {
                cnt++;
                idx++;
                continue;
            }
            if (stack.size() > 0 && stack.peek() == cnt) {
                stack.pop();
                cnt++;
                continue;
            }
            stack.push(num[idx]);
            idx++;
        }
        while (stack.size() > 0)  {
            int tmp = stack.pop();
            if (tmp != cnt) break;
            cnt++;
        }
        System.out.println(cnt - 1 == N ? "Nice" : "Sad");
    }
}

