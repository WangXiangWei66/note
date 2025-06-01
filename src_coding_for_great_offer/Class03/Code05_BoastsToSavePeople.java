package Class03;

import java.util.Arrays;

public class Code05_BoastsToSavePeople {

    public static int numRescueBoats1(int[] arr, int limit) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int N = arr.length;
        Arrays.sort(arr);
        if (arr[N - 1] > limit) {
            return -1;
        }
        int lessR = -1;
        for (int i = N - 1; i >= 0; i--) {
            if (arr[i] <= (limit / 2)) {
                lessR = i;
                break;
            }
        }
        if (lessR == -1) {
            return N;
        }
        int L = lessR;
        int R = lessR + 1;
        int noUsed = 0;//初始化未匹配的人数
        while (L >= 0) {
            int solved = 0;//当前左指针能匹配的人数
            while (R < N && arr[L] + arr[R] <= limit) {
                R++;
                solved++;
            }
            if (solved == 0) {
                noUsed++;
                L--;
            } else {
                L = Math.max(-1, L - solved);//更新一下下一步左指针的位置
            }
        }
        int all = lessR + 1;//记录体重<=limit>>2的总人数
        int used = all - noUsed;//计算已经配对的人数
        int moreUnsolved = (N - all) - used;
        return used + ((noUsed + 1) >> 1) + moreUnsolved;
    }

    public static int numRescueBoats2(int[] people, int limit) {//people为体重数组
        Arrays.sort(people);
        int ans = 0;
        int l = 0;
        int r = people.length - 1;
        int sum = 0;//计算尝试配对的两人的体重之和
        while (l <= r) {
            sum = l == r ? people[l] : people[l] + people[r];
            if (sum > limit) {
                r--;
            } else {
                l++;
                r--;
            }
            ans++;//无论哪一个if成立，都需要准备一条船
        }
        return ans;
    }
}
