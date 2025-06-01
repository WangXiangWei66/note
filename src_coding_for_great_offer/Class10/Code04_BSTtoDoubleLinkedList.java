package Class10;

public class Code04_BSTtoDoubleLinkedList {

    public static class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int data) {
            this.value = data;
        }
    }

    public static Node treeToDoubleList(Node head) {
        if (head == null) {
            return null;
        }
        Info allInfo = process(head);
        allInfo.end.right = allInfo.start;
        allInfo.start.left = allInfo.end;
        return allInfo.start;
    }

    public static class Info {
        //定义了链表的头节点和尾节点
        public Node start;
        public Node end;

        public Info(Node start, Node end) {
            this.start = start;
            this.end = end;
        }
    }

    //使用递归后序遍历的方式，将一棵二叉树转换为一个有序的双向链表
    //转换后的链表顺序与二叉树的中序遍历结果一致
    public static Info process(Node x) {
        if (x == null) {
            return new Info(null, null);
        }
        Info lInfo = process(x.left);
        Info rInfo = process(x.right);
        if (lInfo.end != null) {
            lInfo.end.right = x;
        }
        x.left = lInfo.end;
        x.right = rInfo.start;
        if (rInfo.start != null) {
            rInfo.start.left = x;
        }
        return new Info(lInfo.start != null ? lInfo.start : x, rInfo.end != null ? rInfo.end : x);
    }
}
