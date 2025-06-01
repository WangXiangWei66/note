package Class05;

public class Code03_EditCost {

    public static int minCost1(String s1, String s2, int ic, int dc, int rc) {
        if (s1 == null || s2 == null) {
            return 0;
        }
        char[] str1 = s1.toCharArray();
        char[] str2 = s2.toCharArray();
        int N = str1.length + 1;
        int M = str2.length + 1;
        int[][] dp = new int[N][M];
        for (int i = 1; i < N; i++) {
            dp[i][0] = dc * i;
        }
        for (int j = 1; j < M; j++) {
            dp[0][j] = ic * j;
        }
        for (int i = 1; i < N; i++) {
            for (int j = 1; j < M; j++) {
                dp[i][j] = dp[i - 1][j - 1] + (str1[i - 1] == str2[j - 1] ? 0 : rc);
                dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + ic);
                dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + dc);
            }
        }
        return dp[N - 1][M - 1];
    }

    public static int minCost2(String str1, String str2, int ic, int dc, int rc) {
        if (str1 == null || str2 == null) {
            return 0;
        }
        char[] chs1 = str1.toCharArray();
        char[] chs2 = str2.toCharArray();
        char[] longs = chs1.length >= chs2.length ? chs1 : chs2;
        char[] shorts = chs1.length < chs2.length ? chs1 : chs2;//找出较长字符串和较短字符串
        if (chs1.length < chs2.length) {
            int tmp = ic;
            ic = dc;
            dc = tmp;//如果str1较短，就把插入和删除的代价交换
        }
        int[] dp = new int[shorts.length + 1];//dp来存中间结果
        for (int i = 1; i <= shorts.length; i++) {
            dp[i] = ic * i;//将空字符串转化为前i个字符的最小代价
        }
        for (int i = 1; i <= longs.length; i++) {//外层记录较长字符的每个字符的遍历
            int pre = dp[0];//记录上一行的值
            dp[0] = dc * i;//都删完的代价
            for (int j = 1; j <= shorts.length; j++) {
                int tmp = dp[j];//保存一下当前的值
                if (longs[i - 1] == shorts[j - 1]) {
                    dp[j] = pre;
                } else {
                    dp[j] = pre + rc;
                }
                dp[j] = Math.min(dp[j], dp[j - 1] + rc);
                dp[j] = Math.min(dp[j], tmp + dc);
                pre = tmp;
            }
        }
        return dp[shorts.length];
    }

    public static void main(String[] args) {
        String str1 = "ab12cd3";
        String str2 = "abcdf";
        System.out.println(minCost1(str1, str2, 5, 3, 2));
        System.out.println(minCost2(str1, str2, 5, 3, 2));

        str1 = "abcdf";
        str2 = "ab12cd3";
        System.out.println(minCost1(str1, str2, 5, 3, 2));
        System.out.println(minCost2(str1, str2, 5, 3, 2));


        str1 = "";
        str2 = "ab12cd3";
        System.out.println(minCost1(str1, str2, 5, 3, 2));
        System.out.println(minCost2(str1, str2, 5, 3, 2));

        str1 = "abcdf";
        str2 = "";
        System.out.println(minCost1(str1, str2, 5, 3, 2));
        System.out.println(minCost2(str1, str2, 5, 3, 2));
    }

}
