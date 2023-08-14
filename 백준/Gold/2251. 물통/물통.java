import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

    static int A, B, C;
    static boolean[][] visited;
    static Set<Integer> result;

    public static void main(String[] args) throws IOException {

        visited = new boolean[201][201];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        result = new TreeSet<>();
        dfs(0,0, C);

        for (int answer : result) {
            System.out.print(answer + " ");
        }

    }

    public static void dfs(int a, int b, int c) {
        if (visited[a][b]) return;
        visited[a][b] = true;

        if (a == 0) {
            result.add(c);
        }

        if(a+b > B) {
            dfs((a + b) - B, B, c);
        }else {
            dfs(0, a + b, c);
        }

        if(a+b > A) {
            dfs(A, a + b - A, c);
        }else {
            dfs(a+b, 0, c);
        }

        if(a+c > A) {
            dfs(A, b, a + c - A);
        }else {
            dfs(a + c, b, 0);
        }

        if(b+c > B) 	{
            dfs(a, B, b + c - B);
        }else {
            dfs(a, b + c, 0);
        }

        dfs(a, 0, b + c);
        // 1 -> 2
        dfs(0, b, a + c);
    }
}
