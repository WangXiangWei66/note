package Class05;

public class Code02_LeftRightSameTreeNumber {

    public static class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int v) {
            value = v;
        }
    }
}
//
//    public static int sameNumber1(Node head) {
//        if (head == null) {
//            return 0;
//        }
//        return sameNumber1(head.left) + sameNumber1(head.right) + (same(head.left, head.right) ? 1 : 0);
//    }
//
//    public static boolean same(Node h1, Node h2) {
//        if (h1 == null ^ h2 == null) {//使用异或运算判断是否有且仅有一个为空
//            return false;
//        }
//        if (h1 == null && h2 == null) {
//            return true;
//        }
//        return h1.value == h2.value && same(h1.left, h2.left) && same(h1.right, h2.right);
//    }
//
/// /    public static int sameNumber2(Node head) {
/// /        String algorithm = "SHA-256";
/// ///        Hash hash = new Hash(algorithm);
/// ///        return process(head, hash).ans;
/// /    }
//
//    public static class Info {
//        public int ans;//存储以该节点为根的子树中左右子树结构相同的节点数量
//        public String str;//该子树的哈希编码字符串
//
//        public Info(int a, String s) {
//            ans = a;
//            str = s;
//        }
//    }
//
//    public static Info process(Node head, Hash hash) {
//        if (head == null) {
////            return new Info(0, hash.hashCode("#,"));
//        }
//        Info l = process(head.left, hash);
//        Info r = process(head.right, hash);
//        int ans = (l.str.equals(r.str) ? 1 : 0) + l.ans + r.ans;
////        String str = hash.hashCode(String.valueOf(head.value) + "," + l.str + r.str);//当前节点的哈希编码为当前节点的值，左右子树的哈希编码
////        return new Info(ans, str);
//    }
//
//    public static Node randomBinaryTree(int restLevel, int maxValue) {
//        if (restLevel == 0) {
//            return null;
//        }
//        Node head = Math.random() < 0.2 ? null : new Node((int) (Math.random() * maxValue));
//        if (head != null) {
//            head.left = randomBinaryTree(restLevel - 1, maxValue);
//            head.right = randomBinaryTree(restLevel - 1, maxValue);
//        }
//        return head;
//    }
//
//    public static void main(String[] args) {
//        int maxValue = 8;
//        int maxLevel = 8;
//        int testTime = 10000;
//        System.out.println("test begin");
//        for (int i = 0; i < testTime; i++) {
//            Node head = randomBinaryTree(maxLevel, maxValue);
//            int ans1 = sameNumber1(head);
//            int ans2 = sameNumber2(head);
//            if (ans1 != ans2) {
//                System.out.println("Oops");
//                System.out.println(ans1);
//                System.out.println(ans2);
//            }
//        }
//        System.out.println("test finish");
//    }
//}
