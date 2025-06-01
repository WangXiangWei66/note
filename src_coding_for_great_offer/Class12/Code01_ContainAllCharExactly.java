package Class12;

import java.util.Arrays;

public class Code01_ContainAllCharExactly {

    public static int containExactly1(String s, String a) {
        if (s == null || a == null || s.length() < a.length()) {
            return -1;
        }
        char[] aim = a.toCharArray();
        Arrays.sort(aim);
        String aimSort = String.valueOf(aim);
        for (int L = 0; L < s.length(); L++) {
            for (int R = L; R < s.length(); R++) {
                char[] cur = s.substring(L, R + 1).toCharArray();
                Arrays.sort(cur);
                String curSort = String.valueOf(cur);
                if (curSort.equals(aimSort)) {
                    return L;
                }
            }
        }
        return -1;
    }

    public static int containsExactly2(String s, String a) {
        if (s == null || a == null || s.length() < a.length()) {
            return -1;
        }
        char[] str = s.toCharArray();
        char[] aim = a.toCharArray();
        //L <= str.length - aim.length :
        for (int L = 0; L <= str.length - aim.length; L++) {
            if (isCountEqual(str, L, aim)) {
                return L;
            }
        }
        return -1;
    }

    public static boolean isCountEqual(char[] str, int L, char[] aim) {
        //假设字符集为ASCII 使用数组统计字符频率
        int[] count = new int[256];
        for (int i = 0; i < aim.length; i++) {
            count[aim[i]]++;
        }
        for (int i = 0; i < aim.length; i++) {
            if (count[str[L + i]]-- == 0) {
                return false;
            }
        }
        return true;
    }

    public static int containExactly3(String s1, String s2) {
        if (s1 == null || s2 == null || s1.length() < s2.length()) {
            return -1;
        }
        char[] str2 = s2.toCharArray();
        int M = str2.length;
        int[] count = new int[256];
        for (int i = 0; i < M; i++) {
            count[str2[i]]++;
        }
        int all = M;
        char[] str1 = s1.toCharArray();
        int R = 0;
        for (; R < M; R++) {
            if (count[str1[R]]-- > 0) {
                all--;
            }
        }
        for (; R < str1.length; R++) {
            if (all == 0) {
                return R - M;
            }
            if (count[str1[R]]-- > 0) {
                all--;
            }
            if (count[str1[R - M]]++ >= 0) {
                all++;
            }
        }
        return all == 0 ? R - M : -1;
    }

    public static String getRandomString(int possibilities, int maxSize) {
        char[] ans = new char[(int) (Math.random() * maxSize) + 1];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = (char) ((int) (Math.random() * possibilities) + 'a');
        }
        return String.valueOf(ans);
    }

    public static void main(String[] args) {
        int possibilities = 5;
        int strMaxSize = 20;
        int aimMaxSize = 10;
        int testTime = 500000;
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            String str = getRandomString(possibilities, strMaxSize);
            String aim = getRandomString(possibilities, aimMaxSize);
            int ans1 = containExactly1(str, aim);
            int ans2 = containsExactly2(str, aim);
            int ans3 = containExactly3(str, aim);
            if (ans1 != ans2 || ans1 != ans3) {
                System.out.println("Oops");
                System.out.println(ans1);
                System.out.println(ans2);
                System.out.println(ans3);
                break;
            }
        }
        System.out.println("test finish");
    }
}
