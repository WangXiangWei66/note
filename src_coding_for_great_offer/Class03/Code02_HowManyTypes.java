package Class03;

import java.util.HashSet;

public class Code02_HowManyTypes {//统计字符数组中不同字符集合的数量

    public static int types1(String[] arr) {
        HashSet<String> types = new HashSet<>();//存不同字符的集合
        for (String str : arr) {
            char[] chs = str.toCharArray();
            boolean[] map = new boolean[26];//标记字符是否出现过
            for (int i = 0; i < chs.length; i++) {
                map[chs[i] - 'a'] = true;//将出现过的字母标记为true
            }
            String key = "";//将出现过的字符拼接成一个字符串
            for (int i = 0; i < 26; i++) {
                if (map[i]) {
                    key += String.valueOf((char) (i + 'a'));
                }
            }
            types.add(key);
        }
        return types.size();//返回Hashset的大小
    }

    public static int types2(String[] arr) {
        HashSet<Integer> types = new HashSet<>();
        for (String str : arr) {
            char[] chs = str.toCharArray();
            int key = 0;
            for (int i = 0; i < chs.length; i++) {
                key |= (1 << (chs[i] - 'a'));
            }
            types.add(key);
        }
        return types.size();
    }

    public static String[] getRandomStringArray(int possibilities, int strMaxSize, int arrMaxSize) {
        String[] ans = new String[(int) (Math.random() * arrMaxSize) + 1];//字符数组的范围
        for (int i = 0; i < ans.length; i++) {
            ans[i] = getRandomString(possibilities, strMaxSize);
        }
        return ans;
    }

    public static String getRandomString(int possibilities, int strMaxSize) {
        char[] ans = new char[(int) (Math.random() * strMaxSize) + 1];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = (char) ((int) (Math.random() * possibilities) + 'a');
        }
        return String.valueOf(ans);
    }

    public static void main(String[] args) {
        int possibilities = 5;//可能的字符数量
        int strMaxSize = 10;//字符串的最大长度
        int arrMaxSize = 100;//数组最大长度
        int testTime = 500000;
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            String[] arr = getRandomStringArray(possibilities, strMaxSize, arrMaxSize);
            int ans1 = types1(arr);
            int ans2 = types2(arr);
            if (ans1 != ans2) {
                System.out.println("Oops");
                break;
            }
        }
        System.out.println("test finish");
    }
}
