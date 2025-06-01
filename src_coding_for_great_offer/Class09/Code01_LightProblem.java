package Class09;


public class Code01_LightProblem {

    //no loop
    public static int noLoopRight(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0] == 1 ? 0 : 1;
        }
        if (arr.length == 2) {
            return arr[0] != arr[1] ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        return f1(arr, 0);
    }

    //对于每个元素arr[i]，有两种选择：
    //不修改当前元素，直接处理下一个元素。
    //修改当前元素（通过change1方法），处理下一个元素，然后撤销修改（回溯）。
    //通过比较两种选择的结果，取最小值作为最优解。
    public static int f1(int[] arr, int i) {
        if (i == arr.length) {
            return valid(arr) ? 0 : Integer.MAX_VALUE;//遍历数组的所有元素，看看是否都为0
        }
        int p1 = f1(arr, i + 1);
        change1(arr, i);
        int p2 = f1(arr, i + 1);
        change1(arr, i);//这一步是回溯操作
        p2 = (p2 == Integer.MAX_VALUE) ? p2 : (p2 + 1);
        return Math.min(p1, p2);
    }

    public static void change1(int[] arr, int i) {
        if (i == 0) {
            arr[0] ^= 1;
            arr[1] ^= 1;
        } else if (i == arr.length - 1) {
            arr[i - 1] ^= 1;
            arr[i] ^= 1;
        } else {
            arr[i - 1] ^= 1;
            arr[i] ^= 1;
            arr[i + 1] ^= 1;
        }
    }

    //valid :（文件或票证）有效的；正当的，合理的；合法有效的；计算机系统接受的，被计算机系统认为有效的
    public static boolean valid(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) {
                return false;
            }
        }
        return true;
    }


    //no loop and recursion

    public static int noLoopMinStep1(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0] ^ 1;
        }
        if (arr.length == 2) {
            return arr[0] != arr[1] ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        //no change 0 status
        int p1 = process1(arr, 2, arr[0], arr[1]);
        //change 0 status
        int p2 = process1(arr, 2, arr[0] ^ 1, arr[1] ^ 1);
        if (p2 != Integer.MAX_VALUE) {
            p2++;
        }
        return Math.min(p1, p2);
    }

    public static int process1(int[] arr, int nextIndex, int preStatus, int curStatus) {
        if (nextIndex == arr.length) {
            return preStatus != curStatus ? (Integer.MAX_VALUE) : (curStatus ^ 1);
        }
        if (preStatus == 0) {//此时一定要改变
            curStatus ^= 1;
            int cur = arr[nextIndex] ^ 1;//cur来到下一个位置
            int next = process1(arr, nextIndex + 1, curStatus, cur);
            return next == Integer.MAX_VALUE ? next : (next + 1);
        } else {//这个一定不要改变
            return process1(arr, nextIndex + 1, curStatus, arr[nextIndex]);
        }
    }

    //no loop iteration
    public static int noLoopMinStep2(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0] == 1 ? 0 : 1;
        }
        if (arr.length == 2) {
            return arr[0] != arr[1] ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        int p1 = traceNoLoop(arr, arr[0], arr[1]);
        int p2 = traceNoLoop(arr, arr[0] ^ 1, arr[1] ^ 1);
        p2 = (p2 == Integer.MAX_VALUE) ? p2 : (p2 + 1);
        return Math.min(p1, p2);
    }

    public static int traceNoLoop(int[] arr, int preStatus, int curStatus) {
        //i：从索引 2 开始处理数组（假设前两个元素已通过初始状态处理）。
        //op：记录操作次数。
        int i = 2;
        int op = 0;
        while (i != arr.length) {
            if (preStatus == 0) {
                op++;
                preStatus = curStatus ^ 1;
                curStatus = arr[i++] ^ 1;
            } else {
                preStatus = curStatus;
                curStatus = arr[i++];
            }
        }
        //最后一次可能也需要操作(op + (curStatus ^ 1))
        return (preStatus != curStatus) ? Integer.MAX_VALUE : (op + (curStatus ^ 1));
    }

    //loop in violence
    public static int loopRight(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0] == 1 ? 0 : 1;
        }
        if (arr.length == 2) {
            return arr[0] != arr[1] ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        return f2(arr, 0);
    }

    public static int f2(int[] arr, int i) {
        if (i == arr.length) {
            return valid(arr) ? 0 : Integer.MAX_VALUE;
        }
        int p1 = f2(arr, i + 1);
        change2(arr, i);
        int p2 = f2(arr, i + 1);
        change2(arr, i);//这一步是回溯操作
        p2 = (p2 == Integer.MAX_VALUE) ? p2 : (p2 + 1);
        return Math.min(p1, p2);
    }

    public static void change2(int[] arr, int i) {
        arr[lastIndex(i, arr.length)] ^= 1;
        arr[i] ^= 1;
        arr[nextIndex(i, arr.length)] ^= 1;
    }

    //返回循环数组中索引i的前一个索引
    public static int lastIndex(int i, int N) {
        return i == 0 ? (N - 1) : (i - 1);
    }

    //返回循环数组中索引i的下一个索引
    public static int nextIndex(int i, int N) {
        return i == N - 1 ? 0 : (i + 1);
    }

    //loop recursion
    public static int loopMinStep1(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0] == 1 ? 0 : 1;
        }
        if (arr.length == 2) {
            return arr[0] != arr[1] ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        if (arr.length == 3) {
            return (arr[0] != arr[1] || arr[0] != arr[2]) ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        //0不变 1不变
        int p1 = process2(arr, 3, arr[1], arr[2], arr[arr.length - 1], arr[0]);
        //0改变 1不变
        int p2 = process2(arr, 3, arr[1] ^ 1, arr[2], arr[arr.length - 1] ^ 1, arr[0] ^ 1);
        //0不变 1改变
        int p3 = process2(arr, 3, arr[1] ^ 1, arr[2] ^ 1, arr[arr.length - 1], arr[0] ^ 1);
        //0改变 1改变
        int p4 = process2(arr, 3, arr[1], arr[2] ^ 1, arr[arr.length - 1] ^ 1, arr[0]);
        p2 = p2 != Integer.MAX_VALUE ? (p2 + 1) : p2;
        p3 = p3 != Integer.MAX_VALUE ? (p3 + 1) : p3;
        //p4同时修改了两个位置的值，因此要jia2
        p4 = p4 != Integer.MAX_VALUE ? (p4 + 2) : p4;
        return Math.min(Math.min(p1, p2), Math.min(p3, p4));
    }

    //nextIndex是下一个位置
    //preStatus是上一个位置的状态
    //curStatus是当前位置的状态
    //EndStatus是N-1位置的状态
    public static int process2(int[] arr, int nextIndex, int preStatus, int curStatus, int endStatus, int firstStatus) {
        if (nextIndex == arr.length) {
            return (endStatus != firstStatus || endStatus != preStatus) ? Integer.MAX_VALUE : (endStatus ^ 1);
        }
        //noNextPreStatus：不修改当前元素时的下一个 preStatus。
        //yesNextPreStatus：修改当前元素时的下一个 preStatus。
        int noNextPreStatus = 0;
        int yesNextPreStatus = 0;
        //noNextCurStatus：不修改当前元素时的下一个 curStatus。
        //yesNextCurStatus：修改当前元素时的下一个 curStatus。
        int noNextCurStatus = 0;
        int yesNextCurStatus = 0;
        //noEndStatus：不修改当前元素时的最终状态。
        //yesEndStatus：修改当前元素时的最终状态。
        int noEndStatus = 0;
        int yesEndStatus = 0;
        if (nextIndex < arr.length - 1) {
            noNextPreStatus = curStatus;
            yesNextPreStatus = curStatus ^ 1;
            noNextCurStatus = arr[nextIndex];
            yesNextCurStatus = arr[nextIndex] ^ 1;
        } else if (nextIndex == arr.length - 1) {
            noNextPreStatus = curStatus;
            yesNextPreStatus = curStatus ^ 1;
            noNextCurStatus = endStatus;
            yesNextCurStatus = endStatus ^ 1;
            noEndStatus = endStatus;
            yesEndStatus = endStatus ^ 1;
        }
        if (preStatus == 0) {
            int next = process2(arr, nextIndex + 1, yesNextPreStatus, yesNextCurStatus, nextIndex == arr.length - 1 ? yesEndStatus : endStatus, firstStatus);
            return next == Integer.MAX_VALUE ? next : (next + 1);
        } else {
            return process2(arr, nextIndex + 1, noNextPreStatus, noNextCurStatus, nextIndex == arr.length - 1 ? noEndStatus : endStatus, firstStatus);
        }
    }

    // looping iteration
    public static int loopMinStep2(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0] == 1 ? 0 : 1;
        }
        if (arr.length == 2) {
            return arr[0] != arr[1] ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        if (arr.length == 3) {
            return (arr[0] != arr[1] || arr[0] != arr[2]) ? Integer.MAX_VALUE : (arr[0] ^ 1);
        }
        //0不变 1不变
        int p1 = traceLoop(arr, arr[1], arr[2], arr[arr.length - 1], arr[0]);
        //0改变 1不变
        int p2 = traceLoop(arr, arr[1] ^ 1, arr[2], arr[arr.length - 1] ^ 1, arr[0] ^ 1);
        //0不变 1改变
        int p3 = traceLoop(arr, arr[1] ^ 1, arr[2] ^ 1, arr[arr.length - 1], arr[0] ^ 1);
        //0改变 1改变
        int p4 = traceLoop(arr, arr[1], arr[2] ^ 1, arr[arr.length - 1] ^ 1, arr[0]);
        p2 = p2 != Integer.MAX_VALUE ? (p2 + 1) : p2;
        p3 = p3 != Integer.MAX_VALUE ? (p3 + 1) : p3;
        p4 = p4 != Integer.MAX_VALUE ? (p4 + 2) : p4;
        return Math.min(Math.min(p1, p2), Math.min(p3, p4));
    }

    public static int traceLoop(int[] arr, int preStatus, int curStatus, int endStatus, int firstStatus) {
        //i：从索引 3 开始处理数组（假设前两个元素已通过初始状态处理）。
        //op：记录操作次数。
        int i = 3;
        int op = 0;
        while (i < arr.length - 1) {
            if (preStatus == 0) {
                op++;
                preStatus = curStatus ^ 1;
                curStatus = arr[i++] ^ 1;
            } else {
                preStatus = curStatus;
                curStatus = arr[i++];
            }
        }
        if (preStatus == 0) {
            op++;
            preStatus = curStatus ^ 1;
            endStatus ^= 1;
            curStatus = endStatus;
        } else {
            preStatus = curStatus;
            curStatus = endStatus;
        }
        return (endStatus != firstStatus || endStatus != preStatus) ? Integer.MAX_VALUE : (op + (endStatus ^ 1));
    }

    public static int[] randomArray(int len) {
        int[] arr = new int[len];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * 2);
        }
        return arr;
    }

    public static void main(String[] args) {
        int testTime = 2000;
        int lenMax = 12;
        for (int i = 0; i < testTime; i++) {
            int len = (int) (Math.random() * lenMax);
            int[] arr = randomArray(len);
            int ans1 = noLoopRight(arr);
            int ans2 = noLoopMinStep1(arr);
            int ans3 = noLoopMinStep2(arr);
            if (ans1 != ans2 || ans1 != ans3) {
                System.out.println("Oops");
                System.out.println("Oops");
                System.out.println(ans1);
                System.out.println(ans2);
                System.out.println(ans3);
                break;
            }
        }
        System.out.println("===========");
        for (int i = 0; i < testTime; i++) {
            int len = (int) (Math.random() * lenMax);
            int[] arr = randomArray(len);
            int ans1 = loopRight(arr);
            int ans2 = loopMinStep1(arr);
            int ans3 = loopMinStep2(arr);
            if (ans1 != ans2 || ans1 != ans3) {
                System.out.println("Oops");
                System.out.println(ans1);
                System.out.println(ans2);
                System.out.println(ans3);
                break;
            }
        }
        System.out.println("test end");

        System.out.println("===========");
        //characteristic test
        int len = 1000000000;
        int[] arr = randomArray(len);
        long start = 0;
        long end = 0;
        start = System.currentTimeMillis();
        noLoopMinStep2(arr);
        end = System.currentTimeMillis();
        System.out.println(end - start);

        start = System.currentTimeMillis();
        loopMinStep2(arr);
        end = System.currentTimeMillis();
        System.out.println(end - start);
    }

}
