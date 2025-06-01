package Class07;

public class Code02_BalanceBinaryTree {
    public static class TreeNode{
        public int val;
        public TreeNode left;
        public TreeNode right;

        TreeNode(int val){
            this.val=val;
        }
    }
    public static class Info{
        public boolean isBalenced;
        public int height;
        public Info(boolean i,int h){
            isBalenced=i;
            height = h;
        }
    }
    public static boolean isBalenced(TreeNode root){
        return process(root).isBalenced;
    }
    public static Info process(TreeNode root){
        if(root==null){
            return new Info(true,0);
        }
        Info leftInfo=process(root.left);
        Info rightIfo=process(root.right);
        int height=Math.max(leftInfo.height, rightIfo.height)+1;
        boolean isBalenced=leftInfo.isBalenced&& rightIfo.isBalenced&&Math.abs(leftInfo.height- rightIfo.height)<2;
        return new Info(isBalenced,height);
    }
}
