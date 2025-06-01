package Class01;

import java.util.Arrays;

public class Code06_AOE {

    public static int minAOE1(int[] x, int[] hp, int range) {
        boolean allClear = true;//allClear来判断所有的怪物是否都已经被杀死
        for (int i = 0; i < hp.length; i++) {
            if (hp[i] > 0) {
                allClear = false;
                break;
            }
        }
        if (allClear) {
            return 0;
        } else {
            int ans = Integer.MAX_VALUE;//ans来存储使用的最少技能次数
            for (int left = 0; left < x.length; left++) {//left为每一个可能的起始位置
                if (hasHp(x, hp, left, range)) {//判断这个范围的怪物是否还有生命值
                    minusOneHp(x, hp, left, range);//将所有的怪物的血量减一
                    ans = Math.min(ans, 1 + minAOE1(x, hp, range));//计算剩余情况下的最少使用次数
                    addOneHp(x, hp, left, range);//回复现场的操作
                }
            }
            return ans;
        }
    }

    public static boolean hasHp(int[] x, int[] hp, int left, int range) {
        for (int index = left; index < x.length && x[index] - x[left] <= range; index++) {
            if (hp[index] > 0) {
                return true;
            }
        }
        return false;
    }

    public static void minusOneHp(int[] x, int[] hp, int left, int range) {
        for (int index = left; index < x.length && x[index] - x[left] <= range; index++) {
            hp[index]--;
        }
    }

    public static void addOneHp(int[] x, int[] hp, int left, int range) {
        for (int index = left; index < x.length && x[index] - x[left] <= range; index++) {
            hp[index]++;
        }
    }

    public static int minAOE2(int[] x, int[] hp, int range) {
        int n = x.length;//获取怪物的数量
        int[] cover = new int[n];//覆盖的怪兽末尾位置
        int r = 0;//来遍历每个怪物的位置
        for (int i = 0; i < n; i++) {
            while (r < n && x[r] - x[i] <= range) {
                r++;
            }
            cover[i] = r;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (hp[i] > 0) {
                int minus = hp[i];//需要对当前怪物造成的伤害
                for (int index = i; index < cover[i]; index++) {
                    hp[index] -= minus;
                }
                ans += minus;
            }
        }
        return ans;//返回的是消灭怪物造成的总伤害最小
    }

    public static int minAOE3(int[] x, int[] hp, int range) {
        int n = x.length;
        int[] cover = new int[n];
        int r = 0;//遍历怪物位置数组的指针
        for (int i = 0; i < n; i++) {
            while (r < n && x[r] - x[i] <= range) {
                r++;
            }
            cover[i] = r - 1;//从第i个怪物开始，范围技能能覆盖到的最后一个怪物的索引
        }
        SegmentTree st = new SegmentTree(hp);
        st.build(1, n, 1);
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int leftHp = st.query(i, i, 1, n, 1);
            if (leftHp > 0) {
                ans += leftHp;
                st.add(i, cover[i - 1] + 1, -leftHp, 1, n, 1);
            }
        }
        return ans;
    }

    public static class SegmentTree {
        private int MAXN;//数组的最大长度，是原数组+1
        private int[] arr;//存储原始数据的数组，索引从1开始
        private int[] sum;//存储线段树节点的区间和，线段数的所有节点的数量不会超过4N
        private int[] lazy;//懒标记，存储待更新的值

        public SegmentTree(int[] origin) {
            MAXN = origin.length + 1;
            arr = new int[MAXN];
            for (int i = 1; i < MAXN; i++) {
                arr[i] = origin[i - 1];
            }
            sum = new int[MAXN << 2];
            lazy = new int[MAXN << 2];
        }

        private void pushUp(int rt) {//向上更新节点的区间和
            sum[rt] = sum[rt << 1] + sum[rt << 1 | 1];//rt为当前节点的编号  剩下两个分别是左右子节点
        }

        private void pushDown(int rt, int ln, int rn) {//向下传递懒标记，rt为当前节点编号，ln是左子树的节点数量，rn是右子树节点的数量
            if (lazy[rt] != 0) {
                lazy[rt << 1] += lazy[rt];
                sum[rt << 1] += lazy[rt] * ln;
                lazy[rt << 1 | 1] += lazy[rt];
                sum[rt << 1 | 1] += lazy[rt] * rn;
                lazy[rt] = 0;
            }
        }

        public void build(int l, int r, int rt) {//l和r代表的是区间,rt为当前节点的编号
            if (l == r) {
                sum[rt] = arr[l];//如果已经到叶节点了，就把节点的区间和设为arr[l]
                return;
            }
            int mid = (l + r) >> 1;
            build(l, mid, rt << 1);
            build(mid + 1, r, rt << 1 | 1);
            pushUp(rt);
        }

        public void add(int L, int R, int C, int l, int r, int rt) {
            if (L <= l && r <= R) {
                sum[rt] += C * (r - l + 1);
                lazy[rt] += C;
                return;
            }
            int mid = (l + r) >> 1;
            pushDown(rt, mid - l + 1, r - mid);//先下发懒标记
            if (L <= mid) {
                add(L, R, C, l, mid, rt << 1);
            }
            if (R > mid) {
                add(L, R, C, mid + 1, r, rt << 1 | 1);
            }
            pushUp(rt);
        }

        public int query(int L, int R, int l, int r, int rt) {//查询对应的区间和
            if (L <= l && r <= R) {
                return sum[rt];
            }
            int mid = (l + r) >> 1;
            pushDown(rt, mid - l + 1, r - mid);
            int ans = 0;
            if (L <= mid) {
                ans += query(L, R, l, mid, rt << 1);
            }
            if (R > mid) {
                ans += query(L, R, mid + 1, r, rt << 1 | 1);
            }
            return ans;
        }
    }

    public static int[] generateRandomArray(int n, int valueMax) {
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = (int) (Math.random() * valueMax) + 1;
        }
        return ans;
    }

    public static int[] copyArray(int[] arr) {
        int N = arr.length;
        int[] ans = new int[N];
        for (int i = 0; i < N; i++) {
            ans[i] = arr[i];
        }
        return ans;
    }

    public static void main(String[] args) {
        int N = 50;//定义随机数组的上限
        int X = 500;//定义怪物位置的上限
        int H = 60;//定义怪物生命值的上限
        int R = 10;//定义范围射程技能的上限
        int testTime = 50000;
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            int len = (int) (Math.random() * N) + 1;
            int[] x2 = generateRandomArray(len, X);
            Arrays.sort(x2);
            int[] hp2 = generateRandomArray(len, H);
            int[] x3 = copyArray(x2);
            int[] hp3 = copyArray(hp2);
            int range = (int) (Math.random() * R) + 1;
            int ans2 = minAOE2(x2, hp2, range);
            int ans3 = minAOE3(x3, hp3, range);
            if (ans2 != ans3) {
                System.out.println("Oops");
                break;
            }
        }
        System.out.println("test finish");

        System.out.println("============");
        N = 50000;//定义大规模数据的数组长度
        long start;
        long end;
        int[] x2 = generateRandomArray(N, N);
        Arrays.sort(x2);
        int[] hp2 = new int[N];
        for (int i = 0; i < N; i++) {
            hp2[i] = i * 5 + 10;
        }
        int[] x3 = copyArray(x2);
        int[] hp3 = copyArray(hp2);
        int range = 1000;
        start = System.currentTimeMillis();
        System.out.println(minAOE2(x2, hp2, range));
        end = System.currentTimeMillis();
        System.out.println("运行时间：" + (end - start) + "ms");

        start = System.currentTimeMillis();
        System.out.println(minAOE3(x2, hp2, range));
        end = System.currentTimeMillis();
        System.out.println("运行时间：" + (end - start) + "ms");
    }
}
