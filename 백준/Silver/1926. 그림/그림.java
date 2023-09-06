import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M, answer;
    static int[][] picture;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static Queue<Node> q = new LinkedList<>();
    static List<Integer> result = new ArrayList<>();
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
        M = Integer.parseInt(st.nextToken());
        picture = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                picture[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                bfs(i,j);
            }
        }
        Collections.sort(result, Collections.reverseOrder());
        System.out.println(result.size());
        System.out.println(result.size() == 0 ? 0 : result.get(0));
    }

    private static void bfs(int y, int x) {
        if (picture[y][x] == 0) return;
        picture[y][x] = 0;
        q.offer(new Node(y,x));
        answer = 1;
        while (!q.isEmpty()) {
            Node tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.y + dy[i];
                int new_x = tmp.x + dx[i];
                if (0 > new_y || N <= new_y || 0 > new_x || M <= new_x
                        || picture[new_y][new_x] == 0) continue;
                picture[new_y][new_x] = 0;
                answer++;
                q.offer(new Node(new_y, new_x));
            }
        }
        result.add(answer);
    }
}

