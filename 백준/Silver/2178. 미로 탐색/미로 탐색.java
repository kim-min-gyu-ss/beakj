import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M, answer;
    static int[][] miro;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static Queue<Node> q = new LinkedList<>();
    static class Node {
        int y;
        int x;
        int cnt;
        Node(int y, int x, int cnt) {
            this.y = y;
            this.x = x;
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        miro = new int[N][M];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                miro[i][j] = str.charAt(j) - '0';
            }
        }
        bfs(0,0);
        System.out.println(answer);
    }

    private static void bfs(int y, int x) {
        miro[y][x] = 0;
        q.offer(new Node(y,x,1));
        while (!q.isEmpty()) {
            Node tmp = q.poll();
            if (tmp.y == N - 1 && tmp.x == M - 1) {
                answer = tmp.cnt;
                break;
            }
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.y + dy[i];
                int new_x = tmp.x + dx[i];
                if (0 > new_y || N <= new_y || 0 > new_x || M <= new_x
                        || miro[new_y][new_x] == 0) continue;
                miro[new_y][new_x] = 0;
                q.offer(new Node(new_y, new_x, tmp.cnt + 1));
            }
        }
    }
}

