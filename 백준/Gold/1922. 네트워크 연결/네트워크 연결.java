import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static  int[] parents;
    static int N, M, start, end, wei;
    static List<Node> info = new ArrayList<>();
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
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            wei = Integer.parseInt(st.nextToken());
            info.add(new Node(start,end,wei));
        }
        Collections.sort(info,Comparator.comparing(Node::getWei));
        parents = new int[N + 1];
        for (int i = 0; i < N + 1; i++) {
            parents[i] = i;
        }
        System.out.println(tree());
    }

    private static int find(int x) {
        if (parents[x] == x) return x;
        parents[x] = find(parents[x]);
        return parents[x];
    }
    private static int tree() {
        int result = 0;
        for (Node node : info) {
            int x = find(node.start);
            int y = find(node.end);
            if (x != y) {
                parents[y] = x;
                result += node.wei;
            }
        }
        return result;
    }
}
