package Class07;

import java.util.ArrayList;
import java.util.List;

import static java.util.Collections.copy;

public class Code04_PathSumII {
    public static class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }

        public static List<List<Integer>> pathSum(TreeNode root, int sum) {
            List<List<Integer>> ans = new ArrayList<>();
            if (root == null) {
                return ans;
            }
            ArrayList<Integer> path = new ArrayList<>();
            process(root, path, 0, sum, ans);
            return ans;
        }

        public static void process(TreeNode x, List<Integer> path, int PreSum, int Sum, List<List<Integer>> ans) {
            if (x.left == null && x.right == null) {
                if (PreSum + x.val == Sum) {
                    path.add(x.val);
                    ans.add(copy(path));
                    path.remove(path.size() - 1);
                }
                return;
            }
            //x非叶节点
            path.add(x.val);
            PreSum += x.val;
            if (x.left != null) {
                process(x.left, path, PreSum, Sum, ans);
            }
            if (x.right != null) {
                process(x.right, path, PreSum, Sum, ans);
            }
            path.remove(path.size() - 1);
        }

        private static List<Integer> copy(List<Integer> path) {
            List<Integer> ans = new ArrayList<>();
            for (Integer num : path) {
                ans.add(num);
            }
            return ans;
        }
    }
}
