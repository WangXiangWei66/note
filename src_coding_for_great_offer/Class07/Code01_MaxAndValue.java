package Class07;

public class Code01_MaxAndValue {

    public static int maxAndValue(int[] arr) {
        int N = arr.length;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                max = Math.max(max, arr[i] & arr[j]);
            }
        }
        return max;
    }

    public static int maxAndValue2(int[] arr) {
        int M = arr.length;
        int ans = 0;
        for (int bit = 30; bit >= 0; bit--) {
            int i = 0;//i是遍历数组的指针
            int tmp = M;//tmp保存当前候选元素数量M 的临时值
            while (i < M) {
                if ((arr[i] & (1 << bit)) == 0) {
                    swap(arr, i, --M);
                } else {
                    i++;
                }
            }
            if (M == 2) {
                return arr[0] & arr[1];
            }
            if (M < 2) {
                M = tmp;//回复M为之前的值，继续检查下一位
            } else {
                ans |= (1 << bit);//否则先把这一位的1加入ans中
            }
        }
        return ans;
    }

    public static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    public static int[] randomArray(int size, int range) {
        int[] arr = new int[size];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * range) + 1;
        }
        return arr;
    }

    public static void main(String[] args) {
        int maxSize = 50;
        int range = 30;
        int testTime = 100000;
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            int size = (int) (Math.random() * maxSize) + 2;
            int[] arr = randomArray(size, range);
            int ans1 = maxAndValue(arr);
            int ans2 = maxAndValue2(arr);
            if (ans1 != ans2) {
                System.out.println("Oops");
            }
        }
        System.out.println("test finish");
    }
}
