package Class12;

public class Code04_RegularExpressionMatch {

    public static boolean isMatch1(String str, String pat) {
        char[] s = str.toCharArray();
        char[] p = pat.toCharArray();
        return process1(s, p, 0, 0);
    }

    public static boolean process1(char[] s, char[] p, int i, int j) {
        if (i == s.length) {
            if (j == p.length) {
                return true;
            } else {
                return j + 1 < p.length && p[j + 1] == '*' && process1(s, p, i, j + 2);
            }
        } else if (j == p.length) {
            return false;
        } else {
            if (j + 1 == p.length || p[j + 1] != '*') {
                return (s[i] == p[j] || p[j] == '.') && process1(s, p, i + 1, j + 1);
            } else {
                boolean p1 = process1(s, p, i, j + 2);
                boolean p2 = (s[i] == p[j] || p[j] == '.') && process1(s, p, i + 1, j);
                return p1 || p2;
            }
        }
    }

    public static boolean isMatch2(String str, String pat) {
        char[] s = str.toCharArray();
        char[] p = pat.toCharArray();
        int n = s.length;
        int m = p.length;
        int[][] dp = new int[n + 1][m + 1];
        return process2(s, p, 0, 0, dp);
    }

    public static boolean process2(char[] s, char[] p, int i, int j, int[][] dp) {
        if (dp[i][j] != 0) {
            return dp[i][j] == 1;
        }
        boolean ans;
        if (i == s.length) {
            if (j == p.length) {
                ans = true;
            } else {
                ans = j + 1 < p.length && p[j + 1] == '*' && process2(s, p, i, j + 2, dp);
            }
        } else if (j == p.length) {
            ans = false;
        } else {
            if (j + 1 == p.length || p[j + 1] != '*') {
                ans = (s[i] == p[j] || p[j] == '.') && process2(s, p, i + 1, j + 1, dp);
            } else {
                ans = process2(s, p, i, j + 2, dp) || (s[i] == p[j] || p[j] == '.') && process2(s, p, i + 1, j, dp);
            }
        }
        dp[i][j] = ans ? 1 : 2;
        return ans;
    }

    public static boolean isMatch3(String str, String pat) {
        char[] s = str.toCharArray();
        char[] p = pat.toCharArray();
        int n = s.length;
        int m = p.length;
        boolean[][] dp = new boolean[n + 1][m + 1];
        dp[n][m] = true;
        //处理模式末尾的*号 这个for循环是str为空串
        for (int j = m - 2; j >= 0; j--) {
            dp[n][j] = p[j + 1] == '*' && dp[n][j + 2];
        }
        //从后往前来遍历字符串的每个位置
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (i + 1 == p.length || p[j + 1] != '*') {
                    dp[i][j] = (s[i] == p[j] || p[j] == '.') && dp[i + 1][j + 1];
                } else {
                    dp[i][j] = dp[i][j + 2] || ((s[i] == p[j] || p[j] == '.') && dp[i + 1][j]);
                }
            }
        }
        return dp[0][0];
    }
}
