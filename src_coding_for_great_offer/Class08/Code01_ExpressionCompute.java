package Class08;

import java.util.LinkedList;

public class Code01_ExpressionCompute {

    public static int calculate(String str) {
        return f(str.toCharArray(), 0)[0];//递归函数最后返回数组的第一个元素
    }

    public static int[] f(char[] str, int i) {
        LinkedList<String> queue = new LinkedList<String>();//存储操作数和运算符的队列
        int cur = 0;//临时存储当前要解析的数字
        int[] bra = null;//存储运算的结果和结束位置
        while (i < str.length && str[i] != ')') {
            if (str[i] >= '0' && str[i] <= '9') {
                cur = cur * 10 + str[i++] - '0';//加号后面的操作是把字符转化为对应的数值
            } else if (str[i] != '(') {
                addNum(queue, cur, str[i++]);
                cur = 0;
            } else {
                bra = f(str, i + 1);
                cur = bra[0];//获取计算的结果
                i = bra[1] + 1;//获取括号的结束位置
            }
        }
        addNum(queue, cur, '+');//将最后一个数字和默认的加运算符放入队列
        return new int[]{getAns(queue), i};//返回结果数组 ： 计算结果和当前处理的位置
    }

    public static void addNum(LinkedList<String> queue, int num, char op) {
        if (!queue.isEmpty() && (queue.peekLast().equals("*") || queue.peekLast().equals("/"))) {
            String top = queue.pollLast();
            int pre = Integer.valueOf(queue.pollLast());
            num = top.equals("*") ? (pre * num) : (pre / num);
        }
        queue.addLast(String.valueOf(num));
        queue.addLast(String.valueOf(op));
    }

    public static int getAns(LinkedList<String> queue) {
        int ans = Integer.valueOf(queue.pollFirst());//取出队列第一个元素为初始值
        while (queue.size() > 1) {
            String op = queue.pollFirst();//取出运算符
            int num = Integer.valueOf(queue.pollFirst());//取出操作数
            ans += op.equals("+") ? num : -num;//进行加法或者是减法的运算
        }
        return ans;
    }
}
