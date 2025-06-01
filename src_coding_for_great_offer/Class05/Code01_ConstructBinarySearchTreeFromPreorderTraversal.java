package Class05;

import java.util.Stack;

public class Code01_ConstructBinarySearchTreeFromPreorderTraversal {

    public static class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;

        //提供了三种构造函数来创建节点对象
        public TreeNode() {

        }

        public TreeNode(int val) {
            this.val = val;
        }

        public TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static TreeNode bstFromPreorder1(int[] pre) {
        if (pre == null || pre.length == 0) {
            return null;
        }
        return process1(pre, 0, pre.length - 1);
    }

    public static TreeNode process1(int[] pre, int L, int R) {
        if (L > R) {
            return null;
        }
        int firstBig = L + 1;//初始化第一个比根节点大的位置
        for (; firstBig <= R; firstBig++) {
            if (pre[firstBig] > pre[L]) {
                break;
            }
        }
        TreeNode head = new TreeNode(pre[L]);//创建子树的根节点
        head.left = process1(pre, L + 1, firstBig - 1);
        head.right = process1(pre, firstBig, R);
        return head;
    }

    public static TreeNode bestFromPreorder2(int[] pre) {
        if (pre == null || pre.length == 0) {
            return null;
        }
        int N = pre.length;
        int[] nearBig = new int[N];//用来存每个元素右侧第一个比他大的元素的索引
        for (int i = 0; i < N; i++) {
            nearBig[i] = -1;
        }//初始化都为-1，表示暂未找到
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < N; i++) {
            while (!stack.isEmpty() && pre[stack.peek()] < pre[i]) {
                nearBig[stack.pop()] = i;
            }
            stack.push(i);
        }
        return process2(pre, 0, N - 1, nearBig);
    }

    public static TreeNode process2(int[] pre, int L, int R, int[] nearBig) {
        if (L > R) {
            return null;
        }
        int firstBig = (nearBig[L] == -1 || nearBig[L] > R) ? R + 1 : nearBig[L];
        TreeNode head = new TreeNode(pre[L]);
        head.left = process2(pre, L + 1, firstBig - 1, nearBig);
        head.right = process2(pre, firstBig, R, nearBig);
        return head;
    }

    public static TreeNode bestFromPreOrder3(int[] pre) {
        if (pre == null || pre.length == 0) {
            return null;
        }
        int N = pre.length;
        int[] nearBig = new int[N];
        for (int i = 0; i < N; i++) {
            nearBig[i] = -1;
        }
        int[] stack = new int[N];
        int size = 0;
        for (int i = 0; i < N; i++) {
            while (size != 0 && pre[size - 1] < pre[i]) {
                nearBig[stack[--size]] = i;
            }
            stack[size++] = i;
        }
        return precess3(pre, 0, N - 1, nearBig);
    }

    public static TreeNode precess3(int[] pre, int L, int R, int[] nearBig) {
        if (L > R) {
            return null;
        }
        int firstBig = (nearBig[L] == -1 || nearBig[L] > R) ? R + 1 : nearBig[L];
        TreeNode head = new TreeNode(pre[L]);
        head.left = precess3(pre, L + 1, firstBig - 1, nearBig);
        head.right = precess3(pre, firstBig, R, nearBig);
        return head;
    }
}
