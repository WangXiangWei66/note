package Class08;

import java.util.Arrays;

public class Code04_SnakeGame {

    public static int walk1(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int res = Integer.MIN_VALUE;//调用矩阵的每个位置作为起点
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                int[] ans = process(matrix, i, j);//调用process方法，获取两种状态的最大得分
                res = Math.max(res, Math.max(ans[0], ans[1]));
            }
        }
        return res;
    }

    public static int[] process(int[][] m, int i, int j) {
        if (j == 0) {
            return new int[]{m[i][j], -m[i][j]};
        }
        int[] preAns = process(m, i, j - 1);//获取左侧的状态
        int preUnUse = preAns[0];
        int preUse = preAns[1];
        if (i - 1 >= 0) {//获取左上的状态
            preAns = process(m, i - 1, j - 1);
            preUnUse = Math.max(preUnUse, preAns[0]);
            preUse = Math.max(preUse, preAns[1]);
        }
        if (i + 1 < m.length) {//获取左下的状态
            preAns = process(m, i + 1, j - 1);
            preUnUse = Math.max(preUnUse, preAns[0]);
            preUse = Math.max(preUse, preAns[1]);
        }
        int no = -1;//之前没有使用过能力，当前也不会使用能力
        int yes = -1;
        if (preUnUse >= 0) {
            no = m[i][j] + preUnUse;
            yes = -m[i][j] + preUnUse;//只能从上一列不使用能力转移过来
        }
        if (preUse >= 0) {
            yes = Math.max(yes, m[i][j] + preUse);
        }
        return new int[]{no, yes};
    }

    public static int zuo(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int ans = 0;//调用矩阵的每个位置作为起点
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                Info cur = f(matrix, i, j);
                ans = Math.max(ans, Math.max(cur.no, cur.yes));
            }
        }
        return ans;
    }

    public static class Info {
        public int no;
        public int yes;

        public Info(int n, int y) {
            no = n;
            yes = y;
        }
    }

    public static Info f(int[][] matrix, int i, int j) {
        if (j == 0) {
            int no = Math.max(matrix[i][0], -1);
            int yes = Math.max(-matrix[i][0], -1);
            return new Info(no, yes);
        }
        int preNo = -1;
        int preYes = -1;
        Info pre = f(matrix, i, j - 1);//获取左侧的状态
        preNo = Math.max(pre.no, preNo);
        preYes = Math.max(pre.yes, preYes);
        if (i > 0) {//获取左上的状态
            pre = f(matrix, i - 1, j - 1);
            preNo = Math.max(pre.no, preNo);
            preYes = Math.max(pre.yes, preYes);
        }
        if (i < matrix.length - 1) {//获取左下的状态
            pre = f(matrix, i + 1, j - 1);
            preNo = Math.max(pre.no, preNo);
            preYes = Math.max(preYes, pre.yes);
        }
        int no = preNo == -1 ? -1 : (Math.max(-1, preNo + matrix[i][j]));//之前没有使用过能力，当前也不会使用能力
        int p1 = preYes == -1 ? -1 : (Math.max(-1, preYes + matrix[i][j]));//之前没有使用过能力，当前使用能力
        int p2 = preNo == -1 ? -1 : (Math.max(-1, preNo - matrix[i][j]));
        int yes = Math.max(Math.max(p1, p2), -1);
        return new Info(no, yes);
    }

    public static int walk2(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int max = Integer.MIN_VALUE;//调用矩阵的每个位置作为起点
        int[][][] dp = new int[matrix.length][matrix[0].length][2];
        for (int i = 0; i < dp.length; i++) {
            dp[i][0][0] = matrix[i][0];
            dp[i][0][1] = -matrix[i][0];
            max = Math.max(max, Math.max(dp[i][0][0], dp[i][0][1]));
        }
        for (int j = 1; j < matrix[0].length; j++) {
            for (int i = 0; i < matrix.length; i++) {
                int preUnUse = dp[i][j - 1][0];
                int preUse = dp[i][j - 1][1];
                if (i - 1 >= 0) {//获取左上的状态
                    preUnUse = Math.max(preUnUse, dp[i - 1][j - 1][0]);
                    preUse = Math.max(preUse, dp[i - 1][j - 1][1]);
                }
                if (i + 1 < matrix.length) {//获取左下的状态
                    preUnUse = Math.max(preUnUse, dp[i + 1][j - 1][0]);
                    preUse = Math.max(preUse, dp[i + 1][j - 1][1]);
                }
                dp[i][j][0] = -1;//之前没有使用过能力，当前也不会使用能力
                dp[i][j][1] = -1;
                if (preUnUse >= 0) {
                    dp[i][j][0] = matrix[i][j] + preUnUse;
                    dp[i][j][1] = -matrix[i][j] + preUnUse;//只能从上一列不使用能力转移过来
                }
                if (preUse >= 0) {
                    dp[i][j][1] = Math.max(dp[i][j][1], matrix[i][j] + preUse);
                }
                max = Math.max(max, Math.max(dp[i][j][0], dp[i][j][1]));
            }
        }
        return max;
    }

    public static int[][] generateRandomArray(int row, int col, int value) {
        int[][] arr = new int[row][col];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                arr[i][j] = (int) (Math.random() * value) * (Math.random() > 0.5 ? -1 : 1);
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        int N = 7;
        int M = 7;
        int V = 10;
        int testTimes = 100000;
        for (int i = 0; i < testTimes; i++) {
            int r = (int) (Math.random() * (N + 1));
            int c = (int) (Math.random() * (M + 1));
            int[][] matrix = generateRandomArray(r, c, V);
            int ans1 = zuo(matrix);
            int ans2 = walk2(matrix);
            if (ans1 != ans2) {
                for (int j = 0; j < matrix.length; j++) {
                    System.out.println(Arrays.toString(matrix[j]));//对矩阵的每一行都转化为字符串的形式
                }
                System.out.println("Oops ans1" + ans1 + " ans2" + ans2);
                break;
            }
        }
        System.out.println("finish");
    }
}
