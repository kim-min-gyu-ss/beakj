import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M, start, end, wei, mx;
    static List<Node> info = new ArrayList<>();
    static int[] parents;
    static class Node {
        int start;
        int end;
        int wei;
        public Node(int start, int end, int wei) {
            this.start = start;
            this.end = end;
            this.wei = wei;
        }
        public int getWei() {
            return this.wei;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        parents = new int[N + 1];
        for (int i = 0; i < N + 1; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            wei = Integer.parseInt(st.nextToken());
            info.add(new Node(start,end,wei));
        }
        mx = 0;
        Collections.sort(info,Comparator.comparing(Node::getWei));
        System.out.println(tree(N) - mx);
    }

    private static int find(int x) {
        if (parents[x] == x) return x;
        parents[x] = find(parents[x]);
        return parents[x];
    }
    private static int tree(int N) {
        int result = 0;
        int cnt = 0;
        for (Node node : info) {
            int x = find(node.start);
            int y = find(node.end);
            if (x != y) {
                parents[y] = x;
                result += node.wei;
                mx = Math.max(mx,node.wei);
                cnt++;
            }
        }
        return result;
    }
}
