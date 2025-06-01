package Class05;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Code04_DeleteMinCost {

    public static int minCost1(String s1, String s2) {//枚举s2的左右子序列，按长度从大到小排，检查哪个子序列是s1的字串
        List<String> s2Subs = new ArrayList<>();//创建一个ArrayList来存储s2的所有子序列
        process(s2.toCharArray(), 0, "", s2Subs);//生成s2的所有子序列
        s2Subs.sort(new LenComp());//对这些子序列进行从大到小排序
        for (String str : s2Subs) {//遍历排序好的子序列
            if (s1.indexOf(str) != -1) {//找到第一个s1zi串的子序列
                return s2.length() - str.length();//返回他的长度
            }
        }
        return s2.length();
    }

    public static void process(char[] str2, int index, String path, List<String> list) {
        if (index == str2.length) {
            list.add(path);
            return;
        }//选择当前字符和不选择当前字符两种方法

        process(str2, index + 1, path, list);
        process(str2, index + 1, path + str2[index], list);
    }

    public static int onlyDelete(char[] x, char[] y) {
        if (x.length < y.length) {
            return Integer.MAX_VALUE;
        }
        int N = x.length;
        int M = y.length;
        int[][] dp = new int[N + 1][M + 1];
        for (int i = 0; i <= N; i++) {//初始化所有的值都为系统最大
            for (int j = 0; j <= M; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[0][0] = 0;
        for (int i = 1; i <= N; i++) {
            dp[i][0] = i;
        }
        for (int xlen = 1; xlen <= N; xlen++) {
            for (int ylen = 1; ylen <= Math.min(M, xlen); ylen++) {
                if (dp[xlen - 1][ylen] != Integer.MAX_VALUE) {
                    dp[xlen][ylen] = dp[xlen - 1][ylen] + 1;
                }
                if (x[xlen - 1] == y[ylen - 1] && dp[xlen - 1][ylen - 1] != Integer.MAX_VALUE) {
                    dp[xlen][ylen] = Math.min(dp[xlen][ylen], dp[xlen - 1][ylen - 1]);
                }
            }
        }
        return dp[N][M];
    }

    public static class LenComp implements Comparator<String> {

        @Override
        public int compare(String o1, String o2) {
            return o2.length() - o1.length();
        }
    }

    public static int minCost2(String s1, String s2) {
        if (s1.length() == 0 || s2.length() == 0) {
            return s2.length();
        }
        int ans = Integer.MAX_VALUE;
        char[] str2 = s2.toCharArray();
        for (int start = 0; start < s1.length(); start++) {
            for (int end = start + 1; end <= s1.length(); end++) {
                ans = Math.min(ans, distance(str2, s1.substring(start, end).toCharArray()));
            }
        }
        return ans == Integer.MAX_VALUE ? s2.length() : ans;
    }

    public static int distance(char[] str2, char[] s1sub) {
        int row = str2.length;
        int col = s1sub.length;//获取str2和str1的字串的长度
        int[][] dp = new int[row][col];
        dp[0][0] = str2[0] == s1sub[0] ? 0 : Integer.MAX_VALUE;
        for (int j = 1; j < col; j++) {
            dp[0][j] = Integer.MAX_VALUE;
        }
        for (int i = 1; i < row; i++) {
            dp[i][0] = (dp[i - 1][0] != Integer.MAX_VALUE || str2[i] == s1sub[0]) ? i : Integer.MAX_VALUE;
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                if (dp[i - 1][j] != Integer.MAX_VALUE) {
                    dp[i][j] = dp[i - 1][j] + 1;//可以直接删
                }
                if (str2[i] == s1sub[j] && dp[i - 1][j - 1] != Integer.MAX_VALUE) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][j - 1]);//去继承
                }
            }
        }
        return dp[row - 1][col - 1];
    }

    public static int minCost3(String s1, String s2) {
        if (s1.length() == 0 || s2.length() == 0) {
            return s2.length();
        }
        char[] str2 = s2.toCharArray();
        char[] str1 = s1.toCharArray();
        int M = str2.length;
        int N = str1.length;
        int[][] dp = new int[M][N];
        int ans = M;//初始化最小的删除成本
        for (int start = 0; start < N; start++) {//遍历s1的每个字符为字符串的起始位置
            dp[0][start] = str2[0] == str1[start] ? 0 : M;
            for (int row = 1; row < M; row++) {
                dp[row][start] = (str2[row] == str1[start] || dp[row - 1][start] != M) ? row : M;
            }
            ans = Math.min(ans, dp[M - 1][start]);
            for (int end = start + 1; end < N && end - start < M; end++) {
                int first = end - start;//计算当前字串的长度
                dp[first][end] = (str2[first] == str1[end] && dp[first - 1][end - 1] == 0) ? 0 : M;
                for (int row = first + 1; row < M; row++) {
                    dp[row][end] = M;
                    if (dp[row - 1][end] != M) {
                        dp[row][end] = dp[row - 1][end] + 1;
                    }
                    if (dp[row - 1][end - 1] != M && str2[row] == str1[end]) {
                        dp[row][end] = Math.min(dp[row][end], dp[row - 1][end - 1]);
                    }
                }
                ans = Math.min(ans, dp[M - 1][end]);
            }
        }
        return ans;
    }

    public static int minCostX(String s1, String s2) {//删除的是s2，目标去变成s1
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        int[][] dp = new int[c2.length + 1][c1.length + 1];//dp[i][j]表示将s2 的前 i 个字符转换为 s1 的前 j 个字符的某个子串所需的最小删除成本
        for (int i = 1; i <= c2.length; i++) {
            dp[i][0] = i;
            for (int j = 1; j <= c1.length; j++) {
                if (c2[i - 1] == c1[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i - 1][j] + 1;
                }
            }
        }
        int ans = dp[c2.length][0];
        for (int j = 1; j <= c1.length; j++) {
            ans = Math.min(ans, dp[c2.length][j]);
        }
        return ans;
    }

    public static String generateRandomString(int l, int v) {
        int len = (int) (Math.random() * l);
        char[] str = new char[len];
        for (int i = 0; i < len; i++) {
            str[i] = (char) ('a' + (int) (Math.random() * v));
        }
        return String.valueOf(str);
    }

    public static void main(String[] args) {
        int str1Len = 200;
        int str2Len = 100;
        int V = 5;
        int testTime = 1000;
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            String str1 = generateRandomString(str1Len, V);
            String str2 = generateRandomString(str2Len, V);
//            int ans1 = minCost1(str1, str2);
            int ans2 = minCost2(str1, str2);
            int ans3 = minCost3(str1, str2);
            int ansX = minCostX(str1, str2);
            if (ans2 != ans3 || ans3 != ansX) {
                System.out.println("Oops");
//                System.out.println(ans1);
                System.out.println(ans2);
                System.out.println(ans3);
                System.out.println(ansX);
                break;
            }
        }
        System.out.println("test finsih");
    }
}
