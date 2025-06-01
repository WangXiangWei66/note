package Class04;

import java.util.HashMap;
import java.util.ArrayList;

public class Code01_QueryHobby {

    public static class QueryBox1 {
        private int[] arr;

        public QueryBox1(int[] array) {
            arr = new int[array.length];
            for (int i = 0; i < arr.length; i++) {
                arr[i] = array[i];
            }
        }

        public int query(int L, int R, int v) {
            int ans = 0;
            for (; L <= R; L++) {
                if (arr[L] == v) {
                    ans++;
                }
            }
            return ans;
        }
    }

    public static class QueryBox2 {
        private HashMap<Integer, ArrayList<Integer>> map;

        public QueryBox2(int[] arr) {
            map = new HashMap<>();
            for (int i = 0; i < arr.length; i++) {
                if (!map.containsKey(arr[i])) {
                    map.put(arr[i], new ArrayList<>());
                }
                map.get(arr[i]).add(i);
            }
        }

        public int query(int L, int R, int value) {
            if (!map.containsKey(value)) {
                return 0;
            }
            ArrayList<Integer> indexArr = map.get(value);
            int a = countLess(indexArr, L);//查询<l的下标
            int b = countLess(indexArr, R + 1);//查询<R+1的下标
            return b - a;
        }

        private int countLess(ArrayList<Integer> arr, int limit) {
            int L = 0;
            int R = arr.size() - 1;
            int mostRight = -1;
            while (L <= R) {
                int mid = L + ((R - L) >> 1);
                if (arr.get(mid) < limit) {
                    mostRight = mid;
                    L = mid + 1;
                } else {
                    R = mid - 1;
                }
            }
            return mostRight + 1;//索引是从0开始，但是元素数量是从1开始记录的，因此要+1
        }
    }

    public static int[] generateRandomArray(int len, int value) {
        int[] ans = new int[(int) (Math.random() * len) + 1];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = (int) (Math.random() * value) + 1;
        }
        return ans;
    }


    public static void main(String[] args) {
        int len = 300;
        int value = 20;
        int testTime = 1000;
        int queryTimes = 1000;
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            int[] arr = generateRandomArray(len, value);
            int N = arr.length;
            QueryBox1 box1 = new QueryBox1(arr);
            QueryBox2 box2 = new QueryBox2(arr);
            for (int j = 0; j < queryTimes; j++) {
                int a = (int) (Math.random() * N);
                int b = (int) (Math.random() * N);
                int L = Math.min(a, b);
                int R = Math.max(a, b);
                int v = (int) (Math.random() * value) + 1;
                if (box1.query(L, R, v) != box2.query(L, R, v)) {
                    System.out.println("Oops");
                }
            }
        }
        System.out.println("test end");
    }
}
