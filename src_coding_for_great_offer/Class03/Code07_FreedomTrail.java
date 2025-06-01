package Class03;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.TreeSet;

public class Code07_FreedomTrail {

    public static int findRotateSteps(String r, String k) {//r为给的一个电话字符串，k为目标字符串
        char[] ring = r.toCharArray();
        int N = ring.length;
        HashMap<Character, ArrayList<Integer>> map = new HashMap<>();//键为字符，值为该字符在唤醒字符串中出现的所有索引位置的列表
        for (int i = 0; i < N; i++) {
            if (!map.containsKey(ring[i])) {
                map.put(ring[i], new ArrayList<>());
            }
            map.get(ring[i]).add(i);
        }
        char[] str = k.toCharArray();
        int M = str.length;
        int[][] dp = new int[N][M + 1];//dp[i][j]表示当前指针指向环形字符串的第i个字符，要输入 目标字符串从第j个字符开始的字串所需要的最少步数
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= M; j++) {
                dp[i][j] = -1;
            }
        }
        return process(0, 0, str, map, N, dp);
    }

    public static int process(int preButton, int index, char[] str, HashMap<Character, ArrayList<Integer>> map, int N, int[][] dp) {//preButton当前指针在环形字符串中的位置，index 表示要输入的目标字符串中的字符索引，str是目标字符串的字符索引，map存储每个字符在环形字符串中出现的位置N是环形字符串的长度dp[i][j]表示当前字符串指向环形字符串的第i个字符，要输入目标字符串从第j个字符开始的子串所需的最少步数
        if (dp[preButton][index] != -1) {
            return dp[preButton][index];
        }
        int ans = Integer.MAX_VALUE;
        if (index == str.length) {
            ans = 0;
        } else {
            char cur = str[index];
            ArrayList<Integer> nextPositions = map.get(cur);//获取当前字符在环形字符串出现的位置
            for (int next : nextPositions) {
                int cost = dial(preButton, next, N) + 1 + process(next, index + 1, str, map, N, dp);
                ans = Math.min(ans, cost);
            }
        }
        dp[preButton][index] = ans;
        return ans;
    }

    public static int dial(int i1, int i2, int size) {//计算从i1位置旋转到i2位置需要的最少步数
        return Math.min(Math.abs(i1 - i2), Math.min(i1, i2) + size - Math.max(i1, i2));
    }

    private int ringLength;//环形表盘ring的长度
    private char[] key;//存储目标字符串key转换后的字符数组
    private ArrayList<TreeSet<Integer>> ringSet;//一个长度为26的Arraylist，每个元素是一个有序表，用来存储每个字母在环形表盘中出现的所有位置
    private final HashMap<Integer, Integer> dp = new HashMap<>();

    public int findRotateSteps2(String ring, String key) {
        char[] chars = ring.toCharArray();
        this.key = key.toCharArray();
        ringLength = chars.length;
        ringSet = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            ringSet.add(new TreeSet<>());//为每一个字母都创建一个TreeSet
        }
        for (int i = 0; i < chars.length; i++) {
            ringSet.get(chars[i] - 'a').add(i);
        }
        return findRotateSteps(0, 0);//从目标字符串的第0个字符开始，环形表盘从0开始
    }

    private int findRotateSteps(int kIndex, int cur) {
        if (kIndex == key.length) {
            return 0;
        }
        int k = kIndex * 100 + cur - 1;
        Integer v = dp.get(k);
        if (v != null) {
            return v;
        } else {
            v = Integer.MAX_VALUE;
        }
        TreeSet<Integer> treeSet = ringSet.get(key[kIndex] - 'a');
        Integer floor = treeSet.floor(cur);//算的是逆时针
        if (floor == null) {
            floor = treeSet.last();//因为本身是环形的
        }
        int len = Math.abs(cur - floor);
        len = Math.min(len, ringLength - len);//取顺逆时针的最小值
        v = Math.min(v, len + 1 + findRotateSteps(kIndex + 1, floor));
        Integer ceiling = treeSet.ceiling(cur);//算的是顺时针
        if (ceiling == null) {
            ceiling = treeSet.first();
        }
        len = Math.abs(cur - ceiling);
        len = Math.min(len, ringLength - len);
        v = Math.min(v, len + 1 + findRotateSteps(kIndex + 1, ceiling));
        dp.put(k, v);
        return v;
    }
}
