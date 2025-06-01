package Class06;

public class Code03_MaximumXorWithAnElementFromArray {

    public static int[] maximizeXor(int[] nums, int[][] queries) {//处理所有查询，并返回每个查询对应的最大异或值
        int N = nums.length;
        NumTrie trie = new NumTrie();
        for (int i = 0; i < N; i++) {
            trie.add(nums[i]);
        }
        int M = queries.length;
        int[] ans = new int[M];//存储每个查询结果
        for (int i = 0; i < M; i++) {
            ans[i] = trie.maxXorWithBehindM(queries[i][0], queries[i][1]);//计算最大的异或值
        }
        return ans;
    }

    public static class Node {
        public int min;
        public Node[] nexts;

        public Node() {
            min = Integer.MAX_VALUE;
            nexts = new Node[2];
        }
    }

    public static class NumTrie {
        public Node head = new Node();

        public void add(int num) {
            Node cur = head;
            head.min = Math.min(head.min, num);
            for (int move = 30; move >= 0; move--) {
                int path = ((num >> move) & 1);
                cur.nexts[path] = cur.nexts[path] == null ? new Node() : cur.nexts[path];
                cur = cur.nexts[path];
                cur.min = Math.min(cur.min, num);
            }
        }

        public int maxXorWithBehindM(int x, int m) {//在不大于m的数中找到与x异或结果最大的值
            if (head.min > m) {
                return -1;
            }
            Node cur = head;
            int ans = 0;
            for (int move = 30; move >= 0; move--) {
                int path = (x >> move) & 1;
                int best = (path ^ 1);
                best ^= (cur.nexts[best] == null || cur.nexts[best].min > m) ? 1 : 0;
                ans |= (path ^ best) << move;
                cur = cur.nexts[best];
            }
            return ans;
        }
    }
}
