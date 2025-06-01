package Class03;

import java.util.Arrays;

public class Code06_ClosestSubsequenceSum {

    public static int[] l = new int[1 << 20];
    public static int[] r = new int[1 << 20];//确保由足够的空间存储所有可能的子序列和

    public static int minAbsDifference(int[] nums, int goal) {//一个子序列和目标值最接近的问题
        if (nums == null || nums.length == 0) {
            return goal;
        }
        int le = process(nums, 0, nums.length >> 1, 0, 0, l);//向下取整
        int re = process(nums, nums.length >> 1, nums.length, 0, 0, r);//获取左右两部分子序列和的数量
        Arrays.sort(l, 0, le);//传入要排序的数组，其实索引和结束索引，进行的是升序
        Arrays.sort(r, 0, re--);//--是为了方便处理数组边界
        int ans = Math.abs(goal);//初始化最小绝对差值为目标值的绝对值
        for (int i = 0; i < le; i++) {
            int rest = goal - l[i];
            while (re > 0 && Math.abs(rest - r[re - 1]) <= Math.abs(rest - r[re])) {
                re--;//re初始指向最后一个元素，在右边找最接近的元素
            }
            ans = Math.min(ans, Math.abs(rest - r[re]));
        }
        return ans;
    }

    public static int process(int[] nums, int index, int end, int sum, int fill, int[] arr) {//用于计算给定数组部分的所有子序列的和，并将这些和存储在指定的数组中
        if (index == end) {//nums为原始的整数数组，包含需要处理的元素，index是递归的其实索引 end是递归的结束索引  sum为初始的子序列和 fill是子序列和的数组索引，开始的时候从数组第0个位置开始存储
            arr[fill++] = sum;
        } else {
            fill = process(nums, index + 1, end, sum, fill, arr);
            fill = process(nums, index + 1, end, sum + nums[index], fill, arr);
        }
        return fill;
    }
}
