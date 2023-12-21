import java.util.*;
class Solution {
    static int[] parent;
    public int solution(int n, int[][] costs) {
        parent = new int[n];
        for (int i = 0; i < n; i++)
            parent[i] = i;
        
        Arrays.sort(costs, (o1, o2) -> o1[2] - o2[2]);
        int result = 0;
        for (int i = 0; i < costs.length; i++) {
            int a = costs[i][0];
            int b = costs[i][1];
            int val = costs[i][2];
            if (find(a) != find(b)) {
                union(a, b);
                result += val;
            }
        }
        return result;
    }
    private int find(int a) {
        if (parent[a] == a) {
            return a;
        } else {
            return parent[a] = find(parent[a]);    
        } 
    }
    
    private void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) parent[b] = a;
    }
}