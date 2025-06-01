package Class13;

import java.text.DecimalFormat;

public class Code01_NCardsABWin {

    public static double f1() {
        return p1(0);
    }

    public static double p1(int cur) {
        if (cur >= 17 && cur < 21) {
            return 1.0;
        }
        if (cur >= 21) {
            return 0.0;
        }
        double w = 0.0;
        for (int i = 1; i <= 10; i++) {
            w += p1(cur + i);
        }
        return w / 10;
    }

    public static double f2(int N, int a, int b) {
        if (N < 1 || a >= b || a < 0 || b < 0) {
            return 0.0;
        }
        if (b - a >= N) {
            return 1.0;
        }
        return p2(0, N, a, b);
    }

    public static double p2(int cur, int N, int a, int b) {
        if (cur >= a && cur < b) {
            return 1.0;
        }
        if (cur >= b) {
            return 0.0;
        }
        double w = 0.0;
        for (int i = 1; i <= N; i++) {
            w += p2(cur + i, N, a, b);
        }
        return w / N;
    }

    public static double f3(int N, int a, int b) {
        if (N < 1 || a >= b || a < 0 || b < 0) {
            return 0.0;
        }
        if (b - a >= N) {
            return 1.0;
        }
        return p3(0, N, a, b);
    }

    public static double p3(int cur, int N, int a, int b) {
        if (cur >= a && cur < b) {
            return 1.0;
        }
        if (cur >= b) {
            return 0.0;
        }
        if (cur == a - 1) {
            return 1.0 * (b - a) / N;
        }
        double w = p3(cur + 1, N, a, b) + p3(cur + 1, N, a, b) * N;
        if (cur + 1 + N < b) {
            w -= p3(cur + 1 + N, N, a, b);
        }
        return w / N;
    }

    public static double f4(int N, int a, int b) {
        if (N < 1 || a >= b || a < 0 || b < 0) {
            return 0.0;
        }
        if (b - a >= N) {
            return 1.0;
        }
        double[] dp = new double[b];
        for (int i = a; i < b; i++) {
            dp[i] = 1.0;
        }
        if (a - 1 >= 0) {
            dp[a - 1] = 1.0 * (b - a) / N;
        }
        for (int cur = a - 2; cur >= 0; cur--) {
            double w = dp[cur + 1] + dp[cur + 1] * N;
            if (cur + 1 + N < b) {
                w -= dp[cur + 1 + N];
            }
            dp[cur] = w / N;
        }
        return dp[0];
    }

    public static void main(String[] args) {
        int N = 10;
        int a = 17;
        int b = 21;
        System.out.println(f1());
        System.out.println(f2(N, a, b));
        System.out.println(f3(N, a, b));
        System.out.println(f4(N, a, b));

        int maxN = 15;
        int maxM = 20;
        int testTime = 100000;
        //创建了一个格式化工具，它能够将小数保留四位有效数字，并且会对末尾的零进行自动去除处理
        DecimalFormat df = new DecimalFormat("#.####");
        for (int i = 0; i < testTime; i++) {
            N = (int) (Math.random() * maxN);
            a = (int) (Math.random() * maxM);
            b = (int) (Math.random() * maxM);
            //df.format()方法将函数返回的结果格式化为四位小数的字符串。
            double ans2 = Double.valueOf(df.format(f2(N, a, b)));
            double ans3 = Double.valueOf(df.format(f3(N, a, b)));
            double ans4 = Double.valueOf(df.format(f4(N, a, b)));
            if (ans2 != ans3 || ans2 != ans4) {
                System.out.println("Oops");
                System.out.println(ans2);
                System.out.println(ans3);
                System.out.println(ans4);
                break;
            }
        }
        System.out.println("test finish");

        N = 10000;
        a = 67567;
        b = 72315;
        System.out.println("方法4的答案为:" + f4(N, a, b));
    }
}
