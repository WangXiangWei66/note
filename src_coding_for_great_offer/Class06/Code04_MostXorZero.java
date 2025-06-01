package Class06;

import java.util.ArrayList;//存储划分的子数组的边界索引
import java.util.HashMap;

public class Code04_MostXorZero {
    public static int comparator(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int N = arr.length;//获取数组的长度
        int[] eor = new int[N];//创建长度为N的前缀异或和
        eor[0] = arr[0];
        for (int i = 1; i < N; i++) {
            eor[i] = eor[i - 1] ^ arr[i];
        }
        return process(eor, 1, new ArrayList<>());
    }

    public static int process(int[] eor, int index, ArrayList<Integer> parts) {//index为当前考虑 的数组索引，parts来存划分的子数组的边界索引
        int ans = 0;
        if (index == eor.length) {
            parts.add(eor.length);//将数组的长度加到parts列表里
            ans = eorZeroParts(eor, parts);//获取异或和为零的子数组的数量
            parts.remove(parts.size() - 1);//将添加的元素从pats中移除
        } else {
            int p1 = process(eor, index + 1, parts);
            parts.add(index);
            int p2 = process(eor, index + 1, parts);
            parts.remove(parts.size() - 1);
            ans = Math.max(p1, p2);
        }
        return ans;
    }

    public static int eorZeroParts(int[] eor, ArrayList<Integer> parts) {
        int L = 0;//初始化左边界为0
        int ans = 0;
        for (Integer end : parts) {//索引是划分点索引，子数组结束位置的下一个位置
            if ((eor[end - 1] ^ (L == 0 ? 0 : eor[L - 1])) == 0) {//异或运算有一个特性：若 a ^ b = c，那么 a ^ c = b 且 b ^ c = a
                ans++;
            }
            L = end;
        }
        return ans;
    }

    public static int mostXor(int[] arr) {//使用动态规划与哈希表
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int N = arr.length;
        int[] dp = new int[N];
        //哈希标用于存异或和以及对应最后出现的索引
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int xor = 0;//记录数组从起始位置到当前位置的元素的异或和
        for (int i = 0; i < N; i++) {
            xor ^= arr[i];
            if (map.containsKey(xor)) {
                int pre = map.get(xor);//获取该异或和上衣出现的索引
                dp[i] = pre == -1 ? 1 : (dp[pre] + 1);
            }
            if (i > 0) {
                dp[i] = Math.max(dp[i - 1], dp[i]);//保证每次都是异或和的最大划分数量
            }
            map.put(xor, i);
        }
        return dp[N - 1];
    }

    public static int[] generateRandomArray(int maxSize, int maxValue) {
        int[] arr = new int[(int) ((maxSize + 1) * Math.random())];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) ((maxValue + 1) * Math.random());
        }
        return arr;
    }

    public static void printArray(int[] arr) {
        if (arr == null) {
            return;
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int testTime = 50;
        int maxSize = 30;
        int maxValue = 50;
        boolean succeed = true;
        for (int i = 0; i < testTime; i++) {
            int[] arr = generateRandomArray(maxSize, maxValue);
            int comp = comparator(arr);
            int res = mostXor(arr);
            if (res != comp) {
                succeed = false;
                printArray(arr);
                System.out.println(res);
                System.out.println(comp);
                break;
            }
        }
        System.out.println(succeed ? "Nice!" : "Oops");
    }
}
