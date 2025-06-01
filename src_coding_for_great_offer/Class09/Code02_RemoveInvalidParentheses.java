package Class09;

import java.util.ArrayList;
import java.util.List;
//过两次遍历来处理左右括号的不平衡问题，最终生成所有可能的有效括号组合
public class Code02_RemoveInvalidParentheses {
    //invalid 无效的
    //parentheses 圆括号
    //modify修改 改进
    public static List<String> removeInvalidParentheses(String s) {
        //ans来存储最终有效字符串
        List<String> ans = new ArrayList<>();
        remove(s, ans, 0, 0, new char[]{'(', ')'});
        return ans;
    }
    //checkIndex：从该位置开始检查括号有效性。
    //deleteIndex：从该位置开始尝试删除多余的右括号。
    //par：当前处理的括号类型，初始为['(', ')']。
    public static void remove(String s, List<String> ans, int checkIndex, int deleteIndex, char[] par) {
        for (int count = 0, i = checkIndex; i < s.length(); i++) {
            //s.charAt(i)用于获取字符串s中索引为i位置处的字符
            if (s.charAt(i) == par[0]) {
                count++;
            }
            if (s.charAt(i) == par[1]) {
                count--;
            }
            if (count < 0) {
                for (int j = deleteIndex; j <= i; ++j) {
                    //j == deleteIndex || s.charAt(j-1) != par[1]避免重复删除连续的右括号
                    if (s.charAt(j) == par[1] && (j == deleteIndex || s.charAt(j - 1) != par[1])) {
                        //s.substring取字符串的子串
                        //s.substring(0, j) + s.substring(j + 1, s.length()) ： 他将j位置的字符给删了
                        remove(s.substring(0, j) + s.substring(j + 1, s.length()), ans, i, j, par);
                    }
                }
                return;
            }
        }
        String reversed = new StringBuilder(s).reverse().toString();
        if (par[0] == '(') {
            remove(reversed, ans, 0, 0, new char[]{')', '('});
        } else {
            ans.add(reversed);
        }
    }
}
