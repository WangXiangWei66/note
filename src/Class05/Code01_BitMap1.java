package Class05;

import java.util.HashSet;
import java.util.function.IntToDoubleFunction;

public class Code01_BitMap1 {
    public static class BitMap {
        private long[] bits;

        public BitMap(int max) {
            bits = new long[(max + 64) >> 6];
        }

        public void add(int num) {
            bits[num >> 6] |= (1 << (num & 63));
        }

        public void delete(int num) {
            bits[num >> 6] &= ~(1 << (num & 63));
        }

        public boolean contains(int num) {
            return (bits[num >> 6] & (1 << (num & 63))) != 0;
        }
    }

    public static void main(String[] args) {
        System.out.println("测试开始！");
        int max = 10000;
        HashSet<Integer> set = new HashSet<>();
        BitMap bitMap = new BitMap(max);
        int testTime = 1000000;
        for (int i = 0; i < testTime; i++) {
            int num = (int) (Math.random() * (max + 1));
            double decide = Math.random();
            if (decide < 0.33) {
                bitMap.add(num);
                set.add(num);
            } else if (decide < 0.66) {
                bitMap.delete(num);
                set.remove(num);
            } else {
                if (bitMap.contains(num) != set.contains(num)) ;
                System.out.println("Ops!");
                break;
            }
        }
        for (int num = 0; num <= max; num++) {
            if (bitMap.contains(num) != set.contains(num)) {
                System.out.println("Ops!");
            }
        }
        System.out.println("测试结束!");
    }
}
