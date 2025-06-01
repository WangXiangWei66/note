package Class04;

public class Code03_SubMatrixMaxSum {

    public static int maxSum(int[][] m) {
        if (m == null || m.length == 0 || m[0].length == 0) {
            return 0;
        }
        int N = m.length;
        int M = m[0].length;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < N; i++) {//确定子矩阵的起始行
            int[] s = new int[M];//存储每列元素的累加和
            for (int j = i; j < N; j++) {//存储子矩阵的结束行
                for (int k = 0; k < M; k++) {
                    s[k] += m[j][k];
                }
                max = Math.max(max, maxSubArray(s));
            }
        }
        return max;
    }

    public static int maxSubArray(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int max = Integer.MIN_VALUE;
        int cur = 0;
        for (int i = 0; i < arr.length; i++) {
            cur += arr[i];
            max = Math.max(max, cur);
            cur = cur < 0 ? 0 : cur;
        }
        return max;
    }

    public static int[] getMaxMatrix(int[][] m) {
        int N = m.length;
        int M = m[0].length;
        int max = Integer.MIN_VALUE;
        int cur = 0;//记录当前子矩阵的和
        int a = 0;//左上角的行索引
        int b = 0;//左上角的列索引
        int c = 0;//右下角的行索引
        int d = 0;//右下角的列索引
        for (int i = 0; i < N; i++) {
            int[] s = new int[M];
            for (int j = i; j < N; j++) {
                cur = 0;
                int begin = 0;//子矩阵的其实列索引
                for (int k = 0; k < M; k++) {
                    s[k] += m[j][k];
                    cur += s[k];
                    if (max < cur) {
                        max = cur;
                        a = i;
                        b = begin;
                        c = j;
                        d = k;
                    }
                    if (cur < 0) {
                        cur = 0;
                        begin = k + 1;
                    }
                }
            }
        }
        return new int[]{a, b, c, d};//最后返回的是矩阵左上与右下的坐标
    }
}
