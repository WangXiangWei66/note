package Class02;

public class Code02_Cola {

    public static int right(int m, int a, int b, int c, int x) {//x是可乐的价格
        int[] qian = {100, 50, 10};
        int[] zhang = {c, b, a};
        int puts = 0;
        while (m != 0) {
            int cur = buy(qian, zhang, x);
            if (cur == -1) {
                return -1;
            }
            puts += cur;
            m--;
        }
        return puts;
    }

    public static int buy(int[] qian, int[] zhang, int rest) {
        int first = -1;
        for (int i = 0; i < 3; i++) {
            if (zhang[i] != 0) {
                first = i;
                break;
            }
        }
        if (first == -1) {
            return -1;
        }
        if (qian[first] >= rest) {
            zhang[first]--;
            giveRest(qian, zhang, first + 1, qian[first] - rest, 1);
            return 1;
        } else {
            zhang[first]--;
            int next = buy(qian, zhang, rest - qian[first]);
            if (next == -1) {
                return -1;
            }
            return 1 + next;
        }
    }

    public static int putTimes(int m, int a, int b, int c, int x) {
        int[] qian = {100, 50, 10};
        int[] zhang = {c, b, a};
        int puts = 0;
        int preQianRest = 0;
        int preQianZhang = 0;
        for (int i = 0; i < 3 && m != 0; i++) {
            int curQianFirstBuyZhang = (x - preQianRest + qian[i] - 1) / qian[i];
            if (zhang[i] >= curQianFirstBuyZhang) {
                giveRest(qian, zhang, i + 1, (preQianRest + qian[i] * curQianFirstBuyZhang) - x, 1);
                puts += curQianFirstBuyZhang + preQianZhang;
                zhang[i] -= curQianFirstBuyZhang;
                m--;
            } else {
                preQianRest += qian[i] * zhang[i];
                preQianZhang += zhang[i];
                continue;//程序会跳过之后的代码，进行下一次循环
            }
            int curQianBuyOneColaZhang = (x + qian[i] - 1) / qian[i];
            int curQianBuyColas = Math.min(zhang[i] / curQianBuyOneColaZhang, m);
            int oneTimeRest = qian[i] * curQianBuyOneColaZhang - x;
            giveRest(qian, zhang, i + 1, oneTimeRest, curQianBuyColas);
            puts += curQianBuyOneColaZhang * curQianBuyColas;
            m -= curQianBuyColas;
            zhang[i] -= curQianBuyOneColaZhang * curQianBuyColas;
            preQianRest = qian[i] * zhang[i];
            preQianZhang = zhang[i];
        }
        return m == 0 ? puts : -1;
    }

    public static void giveRest(int[] qian, int[] zhang, int i, int oneTimeRest, int times) {
        for (; i < 3; i++) {//oneTimeRest是买一瓶可乐后找的钱，对他进行拆分，按照指定的倍数来增加面额的张数
            zhang[i] += (oneTimeRest / qian[i]) * times;//先计算出找剩下的钱中当前面额给的数量
            oneTimeRest %= qian[i];
        }
    }

    public static void main(String[] args) {
        int testTime = 1000;
        int zhangMax = 10;
        int colaMax = 10;
        int priceMax = 20;
        System.out.println("如果错误会打印错误数据，否则便是正确");
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            int m = (int) (Math.random() * colaMax);
            int a = (int) (Math.random() * zhangMax);
            int b = (int) (Math.random() * zhangMax);
            int c = (int) (Math.random() * zhangMax);
            int x = ((int) (Math.random() * priceMax) + 1) * 10;
            int ans1 = putTimes(m, a, b, c, x);
            int ans2 = right(m, a, b, c, x);
            if (ans1 != ans2) {
                System.out.println(m);
                System.out.println(a);
                System.out.println(b);
                System.out.println(c);
                System.out.println(x);
                break;
            }
        }
        System.out.println("test finish");
    }
}
