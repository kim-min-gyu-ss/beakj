import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int T,M,N,K,Y,X,result;
    static int[][] baechoo;
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
        T = Integer.parseInt(br.readLine());
        for (int k = 0; k < T; k++) {
            result = 0;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            baechoo = new int[N][M];
            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                Y = Integer.parseInt(st.nextToken());
                X = Integer.parseInt(st.nextToken());
                baechoo[Y][X] = 1;
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    bfs(i,j);
                }
            }
            System.out.println(result);
        }
    }

    private static void bfs(int y, int x) {
        if (baechoo[y][x] == 0) return;
        baechoo[y][x] = 0;
        int cnt = 1;
        q.offer(new Node(y,x));
        while (!q.isEmpty()) {
            Node tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.y + dy[i];
                int new_x = tmp.x + dx[i];
                if (0 > new_y || N <= new_y || 0 > new_x || M <= new_x
                        || baechoo[new_y][new_x] == 0) continue;
                baechoo[new_y][new_x] = 0;
                q.offer(new Node(new_y, new_x));
                cnt++;
            }
        }
        if (cnt != 0) result++;
    }
}

