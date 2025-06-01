package Class02;

import java.util.HashMap;

public class Code03_ReceiveAndPrintOrderLine {

    public static class Node {
        public String info;
        public Node next;

        public Node(String str) {
            info = str;
        }
    }

    public static class MessageBox {
        private HashMap<Integer, Node> headMap;
        private HashMap<Integer, Node> tailMap;
        private int waitPoint;//当前等的信息的序号

        public MessageBox() {
            headMap = new HashMap<Integer, Node>();
            tailMap = new HashMap<Integer, Node>();
            waitPoint = 1;
        }

        public void receive(int num, String info) {
            if (num < 1) {
                return;
            }
            Node cur = new Node(info);
            headMap.put(num, cur);
            tailMap.put(num, cur);
            if (tailMap.containsKey(num - 1)) {
                tailMap.get(num - 1).next = cur;
                tailMap.remove(num - 1);
                headMap.remove(num);
            }
            if (headMap.containsKey(num + 1)) {
                cur.next = headMap.get(num + 1);
                tailMap.remove(num);
                headMap.remove(num + 1);
            }
            if (num == waitPoint) {
                print();
            }
        }

        private void print() {
            Node node = headMap.get(waitPoint);
            headMap.remove(waitPoint);
            while (node != null) {
                System.out.print(node.info + " ");
                node = node.next;
                waitPoint++;
            }
            tailMap.remove(waitPoint - 1);
            System.out.println();
        }
    }

    public static void main(String[] args) {
        MessageBox box = new MessageBox();
        System.out.println("这是2来的时候");
        box.receive(2, "B");
        System.out.println("这是1来的时候");
        box.receive(1, "A");
        box.receive(4, "D");
        box.receive(5, "E");
        box.receive(7, "G");
        box.receive(8, "H");
        box.receive(6, "F");
        box.receive(3, "C");
        box.receive(9, "I");
        box.receive(10, "J");
        box.receive(12, "L");
        box.receive(13, "M");
        box.receive(11, "K");
    }
}
