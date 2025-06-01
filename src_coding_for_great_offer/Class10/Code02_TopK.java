package Class10;

import java.util.*;

public class Code02_TopK {

    private Node[] heap;
    //heapSize记录实际多少数字进入了堆
    private int heapSize;
    //strNodeMap ：节点加次数的词额表
    private HashMap<String, Node> strNodeMap;
    //nodeIndexMap ： 记录节点在堆中的位置
    private HashMap<Node, Integer> nodeIndexMap;
    //堆的比较器，根据次数由小到大排
    private NodeHeapComp comp;
    private TreeSet<Node> treeSet;

    public Code02_TopK(int K) {
        heap = new Node[K];
        heapSize = 0;
        strNodeMap = new HashMap<String, Node>();
        nodeIndexMap = new HashMap<Node, Integer>();
        comp = new NodeHeapComp();
        treeSet = new TreeSet<>(new NodeTreeSetComp());
    }

    //Node 封装成字符串及其出现的次数
    public static class Node {
        public String str;
        public int times;

        public Node(String s, int t) {
            str = s;
            times = t;
        }
    }

    public static class NodeHeapComp implements Comparator<Node> {

        @Override
        public int compare(Node o1, Node o2) {
            //o2.str.compareTo(o1.str)
            //返回负数：o2 应排在 o1 前面（即降序）。
            //返回正数：o1 应排在 o2 前面。
            return o1.times != o2.times ? (o1.times - o2.times) : (o2.str.compareTo(o1.str));
        }
    }

    public static class NodeTreeSetComp implements Comparator<Node> {

        @Override
        public int compare(Node o1, Node o2) {
            return o1.times != o2.times ? (o2.times - o1.times) : (o1.str.compareTo(o2.str));
        }
    }

    public void add(String str) {
        if (heap.length == 0) {
            return;
        }
        Node curNode = null;
        //curNode 在堆上的位置 是preIndex
        int preIndex = -1;
        if (!strNodeMap.containsKey(str)) {
            curNode = new Node(str, 1);
            strNodeMap.put(str, curNode);
            nodeIndexMap.put(curNode, -1);
        } else {
            curNode = strNodeMap.get(str);
            if (treeSet.contains(curNode)) {
                treeSet.remove(curNode);
            }
            curNode.times++;
            preIndex = nodeIndexMap.get(curNode);
        }
        if (preIndex == -1) {
            if (heapSize == heap.length) {
                if (comp.compare(heap[0], curNode) < 0) {
                    treeSet.remove(heap[0]);
                    treeSet.add(curNode);
                    nodeIndexMap.put(heap[0], -1);
                    nodeIndexMap.put(curNode, 0);
                    heap[0] = curNode;
                    heapify(0, heapSize);
                }
            } else {
                treeSet.add(curNode);
                nodeIndexMap.put(curNode, heapSize);
                heap[heapSize] = curNode;
                heapInsert(heapSize++);
            }
        } else {
            treeSet.add(curNode);
            heapify(preIndex, heapSize);
        }
    }

    public List<String> topK() {
        ArrayList<String> ans = new ArrayList<>();
        for (Node node : treeSet) {
            ans.add(node.str);
        }
        return ans;
    }

    private void heapInsert(int index) {
        while (index != 0) {
            int parent = (index - 1) / 2;
            if (comp.compare(heap[index], heap[parent]) < 0) {
                swap(parent, index);
                index = parent;
            } else {
                break;
            }
        }
    }

    private void heapify(int index, int heapSize) {
        int l = index * 2 + 1;
        int r = index * 2 + 2;
        int smallest = index;
        while (l < heapSize) {
            if (comp.compare(heap[l], heap[index]) < 0) {
                smallest = l;
            }
            if (r < heapSize && comp.compare(heap[r], heap[smallest]) < 0) {
                smallest = r;
            }
            if (smallest != index) {
                swap(smallest, index);
            } else {
                break;
            }
            index = smallest;
            l = index * 2 + 1;
            r = index * 2 + 2;
        }
    }

    private void swap(int index1, int index2) {
        nodeIndexMap.put(heap[index1], index2);
        nodeIndexMap.put(heap[index2], index1);
        Node tmp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = tmp;

    }
}
