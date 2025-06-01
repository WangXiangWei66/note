package Class04;

public class Code06_MakeNo {//makeNo为生成长度为size的数组，且不满足等差数列

    public static int[] makeNo(int size) {
        if (size == 1) {
            return new int[]{1};
        }
        int halfSize = (size + 1) / 2;//计算当前数组大小的一半，向上取整：保证size为奇数时，可以合理分配
        int[] base = makeNo(halfSize);//递归，生成大小为halfSize的数组
        int[] ans = new int[size];
        int index = 0;
        for (; index < halfSize; index++) {
            ans[index] = base[index] * 2 - 1;
        }
        for (int i = 0; index < size; index++, i++) {
            ans[index] = base[i] * 2;
        }//数组前半部分填偶数，后半部分填奇数
        return ans;
    }

    public static boolean isValid(int[] arr) {
        int N = arr.length;
        for (int i = 0; i < N; i++) {//确定第一个元素索引
            for (int k = i + 1; k < N; k++) {//第二个元素索引
                for (int j = k + 1; j < N; j++) {
                    if (arr[i] + arr[j] == 2 * arr[k]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("test begin");
        for (int N = 1; N < 1000; N++) {
            int[] arr = makeNo(N);
            if (!isValid(arr)) {
                System.out.println("Oops");
            }
        }
        System.out.println("test finish");
        System.out.println(isValid(makeNo(1042)));
        System.out.println(isValid(makeNo(2981)));
    }
}
