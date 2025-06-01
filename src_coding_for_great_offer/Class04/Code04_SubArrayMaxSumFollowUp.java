package Class04;

public class Code04_SubArrayMaxSumFollowUp {


    public static int rob1(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0];
        }
        int[] dp = new int[arr.length];
        dp[0] = arr[0];
        dp[1] = Math.max(arr[0], arr[1]);
        for (int i = 2; i < arr.length; i++) {
            int p1 = dp[i - 1];
            int p2 = arr[i] + Math.max(dp[i - 2], 0);//和0比较是为了保证不会出现负数累加的情况
            dp[i] = Math.max(p1, p2);
        }
        return dp[arr.length - 1];
    }

    public static int rob2(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int N = arr.length;
        if (N == 1) {
            return arr[0];
        }
        if (N == 2) {
            return Math.max(arr[0], arr[1]);
        }
        int[] dp = new int[N];
        dp[0] = arr[0];
        dp[1] = Math.max(arr[0], arr[1]);
        for (int i = 2; i < N; i++) {
            dp[i] = Math.max(Math.max(dp[i - 1], arr[i]), arr[i] + dp[i - 2]);
        }
        return dp[N - 1];
    }
}
