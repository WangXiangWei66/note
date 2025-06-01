package Class04;

import java.util.*;
import java.util.Map.Entry;//导入专门的Map接口的Entry类，用于后续遍历Map获取键值对

public class Code08_TheSkyLineProblem {

    public static class Node {
        public int x;//x表示坐标
        public boolean isAdd;//是添加(左边界)还是移除（右边界）操作
        public int h;//节点的高度

        public Node(int x, boolean isAdd, int h) {
            this.x = x;
            this.isAdd = isAdd;
            this.h = h;
        }
    }

    public static class NodeComparator implements Comparator<Node> {

        @Override
        public int compare(Node o1, Node o2) {
            return o1.h - o2.h;
        }
    }

    public static List<List<Integer>> getSkyLine(int[][] matrix) {//接受一个二维整数数组作为输入，创建一个二维列表表示天际线的轮廓
        Node[] nodes = new Node[matrix.length * 2];//因为每个建筑物有左右两个边界
        for (int i = 0; i < matrix.length; i++) {//将建筑物左右边界创建Node对象存储再nodes数组中
            nodes[i * 2] = new Node(matrix[i][0], true, matrix[i][2]);
            nodes[i * 2 + 1] = new Node(matrix[i][1], false, matrix[i][2]);
        }
        Arrays.sort(nodes, new NodeComparator());
        TreeMap<Integer, Integer> mapHeightTimes = new TreeMap<>();//记录高度出现的次数
        TreeMap<Integer, Integer> mapXHeight = new TreeMap<>();//每个横坐标对应的最大高度
        for (int i = 0; i < nodes.length; i++) {
            if (nodes[i].isAdd) {
                if (!mapHeightTimes.containsKey(nodes[i].h)) {
                    mapHeightTimes.put(nodes[i].h, 1);
                } else {
                    mapHeightTimes.put(nodes[i].h, mapHeightTimes.get(nodes[i].h) + 1);
                }
            } else {
                if (mapHeightTimes.get(nodes[i].h) == 1) {
                    mapHeightTimes.remove(nodes[i].h);
                } else {
                    mapHeightTimes.put(nodes[i].h, mapHeightTimes.get(nodes[i].h) - 1);
                }
            }
            if (mapHeightTimes.isEmpty()) {
                mapXHeight.put(nodes[i].x, 0);
            } else {
                mapXHeight.put(nodes[i].x, mapHeightTimes.lastKey());//否则将最大键作为横坐标对应的最大高度
            }
        }
        List<List<Integer>> ans = new ArrayList<>();//创二维列表存天际线轮廓
        for (Entry<Integer, Integer> entry : mapXHeight.entrySet()) {
            int curX = entry.getKey();//取出横坐标对应最大高度
            int curMaxHeight = entry.getValue();
            if (ans.isEmpty() || ans.get(ans.size() - 1).get(1) != curMaxHeight) {
                ans.add(new ArrayList<>(Arrays.asList(curX, curMaxHeight)));
            }
        }
        return ans;
    }
}
