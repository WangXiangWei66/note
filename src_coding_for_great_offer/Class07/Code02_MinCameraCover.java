package Class07;

public class Code02_MinCameraCover {

    public static class TreeNode {
        public int value;
        public TreeNode left;
        public TreeNode right;
    }

    public static int minCameraCover1(TreeNode root) {
        Info data = process1(root);
        return (int) Math.min(data.uncovered + 1, Math.min(data.coveredNoCamera, data.coveredHasCamera));
    }

    public static class Info {
        public long uncovered;
        public long coveredNoCamera;
        public long coveredHasCamera;

        public Info(long un, long no, long has) {
            uncovered = un;
            coveredNoCamera = no;
            coveredHasCamera = has;
        }
    }

    public static Info process1(TreeNode X) {
        if (X == null) {
            return new Info(Integer.MAX_VALUE, 0, Integer.MAX_VALUE);
        }

        Info left = process1(X.left);
        Info right = process1(X.right);
        long uncovered = left.coveredNoCamera + right.coveredNoCamera;
        long coveredNoCamera = Math.min(left.coveredHasCamera + right.coveredHasCamera, Math.min(left.coveredHasCamera + right.coveredNoCamera, left.coveredNoCamera + right.coveredHasCamera));
        long coveredHasCamera = Math.min(left.uncovered, Math.min(left.coveredNoCamera, left.coveredHasCamera)) + Math.min(right.uncovered, Math.min(right.coveredNoCamera, right.coveredHasCamera)) + 1;
        return new Info(uncovered, coveredNoCamera, coveredHasCamera);
    }

    public static int minCameraCover2(TreeNode root) {
        Data data = process2(root);
        return data.cameras + (data.status == Status.UNCOVERED ? 1 : 0);
    }

    public static enum Status {//公共静态枚举类型Status，status ： 状况 状态
        UNCOVERED, COVERED_NO_CAMERA, COVERED_HAS_CAMERA;
    }

    public static class Data {
        public Status status;
        public int cameras;

        public Data(Status status, int cameras) {
            this.status = status;
            this.cameras = cameras;
        }
    }

    public static Data process2(TreeNode x) {
        if (x == null) {
            return new Data(Status.COVERED_NO_CAMERA, 0);
        }
        Data left = process2(x.left);
        Data right = process2(x.right);
        int cameras = left.cameras + right.cameras;
        if (left.status == Status.UNCOVERED || right.status == Status.UNCOVERED) {
            return new Data(Status.COVERED_HAS_CAMERA, cameras + 1);
        }
        if (left.status == Status.COVERED_HAS_CAMERA || right.status == Status.COVERED_HAS_CAMERA) {
            return new Data(Status.COVERED_NO_CAMERA, cameras);
        }
        return new Data(Status.UNCOVERED, cameras);
    }
}
