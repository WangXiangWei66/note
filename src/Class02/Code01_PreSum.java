package Class02;

public class Code01_PreSum {
    public static class RangeSum1 {
        private int[] arr;

        public RangeSum1(int[] array) {
            arr = array;
        }

        public int rangeSum(int L, int R) {
            int sum = 0;
            for (int i = L; i <= R; i++) {
                sum += arr[i];
            }
            return sum;
        }
    }

    public static class RangeSum2 {
        private int[] presum;

        //前缀和数组
        public RangeSum2(int[] array) {
            int N = array.length;
            presum = new int[N];
            presum[0] = array[0];
            for (int i = 1; i < N; i++) {
                presum[i] = presum[i - 1] + array[i];
            }
        }

        public int rangeSum(int L, int R) {
            return L == 0 ? presum[R] : presum[R] - presum[L - 1];//L是从零开始的话就直接打印presum的值 否则就相应的减去一个数
        }
    }
}
