import java.util.*;
class Solution {
    static int[][] road;
    public int solution(int m, int n, int[][] puddles) {
        road = new int[n][m];
        
        if(puddles[0].length > 0){
            for(int[] puddle : puddles){
                road[puddle[1] - 1][puddle[0] - 1] = -1;
            }
        }
        for(int i = 1 ;i < n; i++){
            road[i][0] = (road[i][0] == -1 || road[i-1][0] == -1) ? -1 : 1;
        }
        for(int j = 1 ;j < m ;j++){
            road[0][j] = (road[0][j] == -1 || road[0][j-1] == -1) ? -1 : 1;
        }
        for(int i =1;i < n; i++){
            for(int j= 1 ;j < m; j++){
                if(road[i][j] != -1){
                    int a = road[i-1][j] == -1 ? 0 : road[i-1][j];
                    int b = road[i][j-1] == -1 ? 0 : road[i][j-1];   
                    road[i][j] = ((a + b) == 0) ? -1 : (a + b) % 1000000007;   
                }
            }
        }
        return road[n - 1][m - 1] == -1 ? 0 : road[n - 1][m - 1];
    }
}