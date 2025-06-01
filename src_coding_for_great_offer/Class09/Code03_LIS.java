package Class09;

//LIS: longest increasing subsequence
public class Code03_LIS {

    public static int lengthOfLIS(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        //ends[i]: 目前所有长度为 i + 1的递增子序列的最小结尾
        //ends[0] 是长度为 1 的子序列的最小结尾
        //ends[1] 是长度为 2 的子序列的最小结尾
        //ends有效范围是 0... right
        int[] ends = new int[arr.length];
        ends[0] = arr[0];
        //开始的时候right为0，表示有效区只有0到0范围
        //right 指针：标记 ends 数组的有效范围（0 到 right）。
        int right = 0;
        //max为最长递增子序列的长度
        int max = 1;
        for (int i = 1; i < arr.length; i++) {
            int l = 0;
            int r = right;
            while (l <= r) {
                int m = (l + r) / 2;
                if (arr[i] > ends[m]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            //从while出来后，看l的位置
            right = Math.max(right, l);
            ends[l] = arr[i];
            max = Math.max(max, l + 1);
        }
        return max;
    }
}
