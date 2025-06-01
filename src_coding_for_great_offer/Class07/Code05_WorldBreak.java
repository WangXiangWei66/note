package Class07;

import java.util.HashSet;

public class Code05_WorldBreak {

    public static int ways(String str, String[] arr) {
        HashSet<String> set = new HashSet<>();
        for (String candidate : arr) {
            set.add(candidate);
        }
        return process(str, 0, set);
    }

    public static int process(String str, int i, HashSet<String> set) {
        if (i == str.length()) {
            return 1;
        }
        int ways = 0;
        for (int end = i; end < str.length(); end++) {
            String pre = str.substring(i, end + 1);
            if (set.contains(pre)) {
                ways += process(str, end + 1, set);
            }
        }
        return ways;
    }

    public static int ways1(String str, String[] arr) {
        if (str == null || str.length() == 0 || arr == null || arr.length == 0) {
            return 0;
        }
        HashSet<String> map = new HashSet<>();
        for (String s : arr) {
            map.add(s);
        }
        return f(str, map, 0);
    }

    public static int f(String str, HashSet<String> map, int index) {
        if (index == str.length()) {
            return 1;
        }
        int ways = 0;
        for (int end = index; end < str.length(); end++) {
            if (map.contains(str.substring(index, end + 1))) {
                ways += f(str, map, end + 1);
            }
        }
        return ways;
    }

    public static int ways2(String str, String[] arr) {
        if (arr == null || arr.length == 0 || str == null || str.length() == 0) {
            return 0;
        }
        HashSet<String> map = new HashSet<>();
        for (String s : arr) {
            map.add(s);
        }
        int N = str.length();
        int[] dp = new int[N + 1];
        dp[N] = 1;
        for (int i = N - 1; i >= 0; i--) {
            for (int end = i; end < N; end++) {
                if (map.contains(str.substring(i, end + 1))) {//区间为左闭右开
                    dp[i] += dp[end + 1];
                }
            }
        }
        return dp[0];
    }

    public static class Node {
        public boolean end;
        public Node[] nexts;

        public Node() {
            end = false;
            nexts = new Node[26];
        }
    }

    public static int ways3(String str, String[] arr) {
        if (str == null || str.length() == 0 || arr == null || arr.length == 0) {
            return 0;
        }
        Node root = new Node();
        for (String s : arr) {
            char[] chs = s.toCharArray();
            Node node = root;
            int index = 0;
            for (int i = 0; i < chs.length; i++) {
                index = chs[i] - 'a';
                if (node.nexts[index] == null) {
                    node.nexts[index] = new Node();
                }
                node = node.nexts[index];
            }
            node.end = true;
        }
        return g(str.toCharArray(), root, 0);
    }

    public static int g(char[] str, Node root, int i) {
        if (i == str.length) {
            return 1;
        }
        int ways = 0;
        Node cur = root;
        for (int end = i; end < str.length; end++) {
            int path = str[end] - 'a';
            if (cur.nexts[path] == null) {
                break;
            }
            cur = cur.nexts[path];
            if (cur.end) {
                ways += g(str, root, end + 1);
            }
        }
        return ways;
    }

    public static int ways4(String s, String[] arr) {
        if (s == null || s.length() == 0 || arr == null || arr.length == 0) {
            return 0;
        }
        Node root = new Node();
        for (String str : arr) {
            char[] chs = str.toCharArray();
            Node node = root;
            int index = 0;
            for (int i = 0; i < chs.length; i++) {
                index = chs[i] - 'a';
                if (node.nexts[index] == null) {
                    node.nexts[index] = new Node();
                }
                node = node.nexts[index];
            }
            node.end = true;
        }
        char[] str = s.toCharArray();
        int N = str.length;
        int[] dp = new int[N + 1];
        dp[N] = 1;
        for (int i = N - 1; i >= 0; i--) {
            Node cur = root;
            for (int end = i; end < N; end++) {
                int path = str[end] - 'a';
                if (cur.nexts[path] == null) {
                    break;
                }
                cur = cur.nexts[path];
                if (cur.end) {
                    dp[i] += dp[end + 1];
                }
            }
        }
        return dp[0];
    }

    public static class RandomSample {
        public String str;
        public String[] arr;

        public RandomSample(String s, String[] a) {
            str = s;
            arr = a;
        }
    }

    public static RandomSample generateRandomSample(char[] candidate, int num, int len, int joint) {
        String[] seeds = randomSeeds(candidate, num, len);//从给定字符数组中生成指定数量和长度的随机字符串种子
        HashSet<String> set = new HashSet<>();//num代表生成的随机字符串的数量，len代表每个随机字符串的长度，joint代表要从随机字符串中随机选取多少个进行拼接
        for (String str : seeds) {
            set.add(str);//对种子去重
        }
        String[] arr = new String[set.size()];
        int index = 0;
        for (String str : set) {
            arr[index++] = str;//将不重复的种子存入数组
        }
        StringBuilder all = new StringBuilder();
        for (int i = 0; i < joint; i++) {
            all.append(arr[(int) (Math.random() * arr.length)]);//对字符串进行随机拼接
        }
        return new RandomSample(all.toString(), arr);
    }

    public static String[] randomSeeds(char[] candidates, int num, int len) {
        String[] arr = new String[(int) (Math.random() * num) + 1];//数组的大小是随机的
        for (int i = 0; i < arr.length; i++) {
            char[] str = new char[(int) (Math.random() * len) + 1];
            for (int j = 0; j < str.length; j++) {
                str[j] = candidates[(int) (Math.random() * candidates.length)];
            }
            arr[i] = String.valueOf(str);
        }
        return arr;
    }

    public static void main(String[] args) {
        char[] candidates = {'a', 'b'};
        int num = 20;
        int len = 4;
        int joint = 5;
        int testTime = 3000;
        boolean testResult = true;
        for (int i = 0; i < testTime; i++) {
            RandomSample sample = generateRandomSample(candidates, num, len, joint);
            int ans1 = ways1(sample.str, sample.arr);
            int ans2 = ways2(sample.str, sample.arr);
            int ans3 = ways3(sample.str, sample.arr);
            int ans4 = ways4(sample.str, sample.arr);
            if (ans1 != ans2 || ans2 != ans3 || ans3 != ans4) {
                testResult = false;
            }
        }
        System.out.println(testResult);
    }
}
