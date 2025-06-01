package Class03;

public class Code01_LongestSubstringWithoutRepeaingCharacters {

    public static int lengthOfLongestSubstring(String s) {
        if (s == null || s.equals("")) {
            return 0;
        }
        char[] str = s.toCharArray();
        int[] map = new int[256];//记录每一个字符上一个出现的位置
        for (int i = 0; i < 256; i++) {
            map[i] = -1;//-1表示字符还没有出现过
        }
        map[str[0]] = 0;//记录第一个字符出现的位置
        int N = str.length;
        int ans = 1;//记录不包含重复字符的最长字串的长度
        int pre = 1;
        for (int i = 1; i < N; i++) {
            pre = Math.min(i - map[str[i]], pre + 1);
            ans = Math.max(ans, pre);
            map[str[i]] = i;
        }
        return ans;
    }
}
