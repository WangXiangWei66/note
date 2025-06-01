package Class10;

public class Code01_jumpGame {

    public static int jump(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        //step   记录跳跃次数
        //cur    当前跳跃能到达的最远位置
        // next  下一步跳跃能到达的最远位置
        int step = 0;
        int cur = 0;
        int next = 0;
        for (int i = 0; i < arr.length; i++) {
            if (cur < i) {
                //如果当前位置超出了当前跳跃能到达的最远位置
                //说明需要进行一次跳跃，并更新当前能到达的最远位置
                step++;
                cur = next;
            }
            next = Math.max(next, i + arr[i]);
        }
        return step;
    }
}
