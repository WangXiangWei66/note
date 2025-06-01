package Class09;

import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;

public class Code04_EnvelopeProblem {

    public static int maxEnvelopes(int[][] matrix) {
        Envelop[] arr = sort(matrix);
        int[] ends = new int[matrix.length];
        //ends[i] 表示长度为 i+1 的递增子序列的最小结尾高度
        ends[0] = arr[0].h;
        //right 指针：标记 ends 数组的有效范围（0 到 right）
        int right = 0;
        int l = 0;
        int r = 0;
        int m = 0;
        for (int i = 1; i < arr.length; i++) {
            l = 0;
            r = right;
            while (l <= r) {
                m = (l + r) / 2;
                if (arr[i].h > ends[m]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            right = Math.max(right, l);
            ends[l] = arr[i].h;
        }
        return right + 1;
    }

    public static class Envelop {
        public int l;
        public int h;

        public Envelop(int weight, int height) {
            l = weight;
            h = height;
        }
    }

    public static class EnvelopComparator implements Comparator<Envelop> {
        //长度由小到大，高度由大到小
        @Override
        public int compare(Envelop o1, Envelop o2) {
            return o1.l != o2.l ? o1.l - o2.l : o2.h - o1.h;
        }
    }

    public static Envelop[] sort(int[][] matrix) {
        Envelop[] res = new Envelop[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            res[i] = new Envelop(matrix[i][0], matrix[i][1]);
        }
        Arrays.sort(res, new EnvelopComparator());
        return res;
    }
}
