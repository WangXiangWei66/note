package Class04;

public class Code05_CandyProblem {

    public static int candy1(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int N = arr.length;
        int[] left = new int[N];
        for (int i = 1; i < N; i++) {
            if (arr[i - 1] < arr[i]) {
                left[i] = left[i - 1] + 1;//if条件不成立，最后结果是0
            }
        }
        int[] right = new int[N];
        for (int i = N - 2; i >= 0; i--) {
            if (arr[i] > arr[i + 1]) {
                right[i] = right[i + 1] + 1;
            }
        }
        int ans = 0;
        for (int i = 0; i < N; i++) {
            ans += Math.max(left[i], right[i]);
        }
        return ans + N;//每个孩子最少都会分一个
    }

    public static int candy2(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int index = nextMinIndex2(arr, 0);//找到索引从0开始 的下一个局部最小是的索引
        int res = rightCandas(arr, 0, index++);//计算从索引0到局部最小值索引这一段需要的糖果数
        int lBase = 1;//记录当前递增序列的基础糖果数，初始为1
        int next = 0;//用于存储下一个局部最小值的索引
        int rCands = 0;//记录递减序列所需的糖果数
        int rBase = 0;//递减序列的基础糖果数
        while (index != arr.length) {
            if (arr[index] > arr[index - 1]) {
                res += ++lBase;
                index++;
            } else if (arr[index] < arr[index - 1]) {
                next = nextMinIndex2(arr, index - 1);//找到从index-1开始的下一个局部最小值的索引
                rCands = rightCandas(arr, index - 1, next++);//计算从index-1到下一个局部最小值这一段递减序列所需的糖果数
                rBase = next - index + 1;//递减序列的基础糖果数
                res += rCands + (rBase > lBase ? -lBase : rBase);//累加递减序列可能的糖果数，同时处理可能的重复计算部分
                lBase = 1;//重置递增序列的糖果数
                index = next;//将索引移动到下一个局部最小值之后的位置
            } else {
                res += 1;
                lBase = 1;
                index++;
            }
        }
        return res;
    }

    public static int nextMinIndex2(int[] arr, int start) {
        for (int i = start; i != arr.length - 1; i++) {
            if (arr[i] <= arr[i + 1]) {
                return i;
            }
        }
        return arr.length - 1;
    }

    public static int rightCandas(int[] arr, int left, int right) {
        int n = right - left + 1;
        return n + n * (n - 1) / 2;
    }

    public static int candy3(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int index = nextMinIndex3(arr, 0);
        int[] data = rightCandsAndBase(arr, 0, index++);//获取塘果总数和基础糖果数
        int res = data[0];//初始化第一次糖果总数
        int lBase = 1;
        int same = 1;//连续 相同评分孩子的数量
        int next = 0;//下一个局部最小值的索引
        while (index != arr.length) {
            if (arr[index] > arr[index - 1]) {
                res += ++lBase;
                same = 1;
                index++;
            } else if (arr[index] < arr[index - 1]) {
                next = nextMinIndex3(arr, index - 1);
                data = rightCandsAndBase(arr, index - 1, next++);
                if (data[1] <= lBase) {//如果递减学列的基础糖果数<=递增序列的基础糖果数
                    res += data[0] - data[1];//对糖果总数-递增序列的糖果数累加
                } else {
                    res += -lBase * same + data[0] - data[1] + data[1] * same;//res到目前为止，总共需要的糖果数
                }
                index = next;
                lBase = 1;
                same = 1;
            } else {
                res += lBase;
                same++;
                index++;
            }
        }
        return res;
    }

    public static int nextMinIndex3(int[] arr, int start) {
        for (int i = start; i != arr.length - 1; i++) {
            if (arr[i] < arr[i + 1]) {
                return i;
            }
        }
        return arr.length - 1;
    }

    public static int[] rightCandsAndBase(int[] arr, int left, int right) {//从left到index期间孩子所需的糖果数以及该区间最后一个孩子应分配的糖果数
        int base = 1;//最后一个孩子至少有一个糖果
        int candas = 1;//初始化糖果总数
        for (int i = right - 1; i >= left; i--) {
            if (arr[i] == arr[i + 1]) {
                candas += base;
            } else {
                candas += ++base;
            }
        }
        return new int[]{candas, base};//返回包含糖果总数和基础糖果数的整数数组
    }

    public static void main(String[] args) {
        int[] test1 = {3, 0, 5, 5, 4, 4, 0};
        System.out.println(candy2(test1));

        int[] test2 = {3, 0, 5, 5, 4, 4, 0};
        System.out.println(candy2(test2));
    }
}
