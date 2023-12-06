import java.util.*;
class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        sortArray(data, col);
        int[] answer = getArrays(data, row_begin, row_end);
        return dataToXor(answer);
    }
    
    private void sortArray(int[][] data, int col) {
        Arrays.sort(data, (o1, o2) -> {
            if (o1[col - 1] == o2[col - 1]) {
                return o2[0] - o1[0];
            }
            return o1[col - 1] - o2[col - 1];
        });
    }
    
    private int[] getArrays(int[][] data, int row_begin, int row_end) {
        int[] result = new int[row_end - row_begin + 1];
        int cnt = 0;
        int ln = data[0].length;
        for (int i = row_begin - 1; i < row_end; i++) {
            int tmp = 0;
            for (int j = 0; j < ln; j++) {
                tmp += data[i][j] % (i + 1);
            }
            result[cnt] = tmp;
            cnt++;
        }
        return result;
    }
    
    private int dataToXor(int[] datas) {
        int result = datas[0];
        for (int i = 1; i < datas.length; i++) {
            result ^= datas[i];
        }
        return result;
    }
}