import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, mx ,answer, result, dap;
    static int[][] rain, copy;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static Queue<Node> q = new LinkedList<>();
    static class Node {
        int y;
        int x;
        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        copy = new int[N][N];
        mx = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                copy[i][j] = tmp;
                mx = Math.max(mx,tmp);
            }
        }
        int cnt = 1;
        dap = 0;
        while(cnt < mx) {
            rain = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    rain[i][j] = copy[i][j];
                }
            }



            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (rain[i][j] <= cnt) {
                        rain[i][j] = 0;
                    }
                }
            }
            result = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    int ct = bfs(i,j);
                    if (ct > 0) {
                        result++;
                    }
                }
            }
            cnt++;
            dap = Math.max(dap,result);
        }
        System.out.println(dap != 0 ? dap : 1);
    }

    private static int bfs(int y, int x) {
        if (rain[y][x] == 0) return 0;
        rain[y][x] = 0;
        q.offer(new Node(y,x));
        answer = 1;
        while (!q.isEmpty()) {
            Node tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.y + dy[i];
                int new_x = tmp.x + dx[i];
                if (0 > new_y || N <= new_y || 0 > new_x || N <= new_x
                        || rain[new_y][new_x] == 0) continue;
                rain[new_y][new_x] = 0;
                answer++;
                q.offer(new Node(new_y, new_x));
            }
        }
        return answer;
    }
}

