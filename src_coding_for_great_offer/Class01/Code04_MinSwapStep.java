package Class01;

public class Code04_MinSwapStep {

    public static int minStep1(String s) {
        if (s == null || s.equals("")) {//检查是否为空字符串
            return 0;
        }
        char[] str = s.toCharArray();
        int step1 = 0;//将G移动到一起所需要的步数
        int gi = 0;//记录G所在的位置
        int step2 = 0;//将B移动到一起所需要的步数
        int bi = 0;//记录B所在的位置
        for (int i = 0; i < str.length; i++) {
            if (str[i] == 'G') {
                step1 += i - (gi++);
            } else {
                step2 += i - (bi++);
            }
        }
        return Math.min(step1, step2);
    }

    public static int minStep2(String s) {
        if (s == null || s.equals("")) {
            return 0;
        }
        char[] str = s.toCharArray();
        int step1 = 0;
        int gi = 0;
        for (int i = 0; i < str.length; i++) {
            if (str[i] == 'G') {
                step1 += i - (gi++);
            }
        }
        int step2 = 0;
        int bi = 0;
        for (int i = 0; i < str.length; i++) {
            if (str[i] == 'B') {
                step2 += i - (bi++);
            }
        }
        return Math.min(step1, step2);
    }

    public static String randomString(int maxLen) {
        char[] str = new char[(int) (Math.random() * maxLen)];
        for (int i = 0; i < str.length; i++) {
            str[i] = Math.random() < 0.5 ? 'G' : 'B';
        }
        return String.valueOf(str);
    }

    public static void main(String[] args) {
        int maxLen = 100;
        int testTime = 100000;
        System.out.println("test begin");
        for (int i = 0; i < testTime; i++) {
            String str = randomString(maxLen);
            int ans1 = minStep1(str);
            int ans2 = minStep2(str);
            if (ans1 != ans2) {
                System.out.println("Oops");
                break;
            }
        }
        System.out.println("test finish");
    }
}
