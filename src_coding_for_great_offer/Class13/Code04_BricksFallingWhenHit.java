package Class13;

public class Code04_BricksFallingWhenHit {

    public static int[] hitBricks(int[][] grid, int[][] hits) {
        for (int i = 0; i < hits.length; i++) {
            if (grid[hits[i][0]][hits[i][1]] == 1) {
                grid[hits[i][0]][hits[i][1]] = 2;
            }
        }
        UnionFind unionFind = new UnionFind(grid);
        int[] ans = new int[hits.length];
        for (int i = hits.length - 1; i >= 0; i--) {
            if (grid[hits[i][0]][hits[i][1]] == 2) {
                ans[i] = unionFind.finger(hits[i][0], hits[i][1]);
            }
        }
        return ans;
    }

    public static class UnionFind {
        private int N;
        private int M;
        //cellingALL：与顶部相连的砖块总数
        private int cellingAll;
        private int[][] grid;
        //cellingSet ： ; // 标记每个集合是否与顶部相连
        private boolean[] cellingSet;
        //并查集父节点数组
        private int[] fatherMap;
        //每个集合的大小
        private int[] sizeMap;
        //路径压缩用的栈
        private int[] stack;

        public UnionFind(int[][] matrix) {
            //初始化空间和变量
            initSpace(matrix);
            //初始化连通关系
            initConnect();
        }

        private void initSpace(int[][] matrix) {
            //存储原始网格数据
            grid = matrix;
            N = grid.length;
            M = grid[0].length;
            //网格总单元格数（N * M）
            int all = N * M;
            cellingAll = 0;
            cellingSet = new boolean[all];
            fatherMap = new int[all];
            sizeMap = new int[all];
            //用于在查找操作中压缩路径，提高后续查询效率
            stack = new int[all];
            for (int row = 0; row < N; row++) {
                for (int col = 0; col < M; col++) {
                    if (grid[row][col] == 1) {
                        //二维坐标 (row, col) 映射为一维索引
                        int index = row * M + col;
                        fatherMap[index] = index;
                        sizeMap[index] = 1;
                        if (row == 0) {
                            cellingSet[index] = true;
                            cellingAll++;
                        }
                    }
                }
            }
        }

        //尝试与上下左右的位置进行合并
        private void initConnect() {
            for (int row = 0; row < N; row++) {
                for (int col = 0; col < M; col++) {
                    union(row, col, row - 1, col);
                    union(row, col, row + 1, col);
                    union(row, col, row, col - 1);
                    union(row, col, row, col + 1);
                }
            }
        }

        private int find(int row, int col) {
            //路径上经过节点的数量为stackSize
            int stackSize = 0;
            int index = row * M + col;
            while (index != fatherMap[index]) {
                //当前节点不是父节点，将他先压入栈中
                stack[stackSize++] = index;
                index = fatherMap[index];
            }
            while (stackSize != 0) {
                //将弹出节点的父节点直接设为根节点
                fatherMap[stack[--stackSize]] = index;
            }
            return index;
        }

        private void union(int r1, int c1, int r2, int c2) {
            if (valid(r1, c1) && valid(r2, c2)) {
                int father1 = find(r1, c1);
                int father2 = find(r2, c2);
                if (father1 != father2) {
                    int size1 = sizeMap[father1];
                    int size2 = sizeMap[father2];
                    //两个集合是否和顶部相连
                    boolean status1 = cellingSet[father1];
                    boolean status2 = cellingSet[father2];
                    if (size1 <= size2) {
                        fatherMap[father1] = father2;
                        sizeMap[father2] = size1 + size2;
                        //如果两个集合只有一个是和顶部相连的
                        if (status1 ^ status2) {
                            cellingSet[father2] = true;
                            cellingAll += status1 ? size2 : size1;
                        }
                    } else {
                        fatherMap[father2] = father1;
                        sizeMap[father1] = size1 + size2;
                        if (status1 ^ status2) {
                            cellingSet[father1] = true;
                            cellingAll += status1 ? size2 : size1;
                        }
                    }
                }
            }
        }

        private boolean valid(int row, int col) {
            return row >= 0 && row < N && col >= 0 && col < M && grid[row][col] == 1;
        }

        public int cellingNum() {
            return cellingAll;
        }

        public int finger(int row, int col) {
            grid[row][col] = 1;
            int cur = row * M + col;
            if (row == 0) {
                cellingSet[cur] = true;
                cellingAll++;
            }
            fatherMap[cur] = cur;
            sizeMap[cur] = 1;
            //后续通过与合并后的总数对比，计算增量
            int pre = cellingAll;
            union(row, col, row - 1, col);
            union(row, col, row + 1, col);
            union(row, col, row, col - 1);
            union(row, col, row, col + 1);
            //若新砖块连接了原本不与顶部相连的集合，cellingAll 会增加
            int now = cellingAll;
            if (row == 0) {
                return now - pre;
            } else {
                return now == pre ? 0 : now - pre - 1;
            }
        }
    }
}
