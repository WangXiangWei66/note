package Class01;

import java.io.File;//处理文件和目录的类
import java.util.Stack;//栈结构方便进行深度优先搜索

public class Code02_CountFiles {

    public static int getFileNumber(String folderPath) {//folderPath表示文件夹或者是文件的路径
        File root = new File(folderPath);//由传入的路径创建一个File对象
        if (!root.isDirectory() && !root.isFile()) {
            return 0;
        }
        if (root.isFile()) {
            return 1;
        }
        Stack<File> stack = new Stack<>();
        stack.add(root);
        int files = 0;
        while (!stack.isEmpty()) {
            File folder = stack.pop();
            for (File next : folder.listFiles()) {//listFiles主要用于返回指定目录下的文件和子目录的抽象数组
                if (next.isFile()) {
                    files++;
                }
                if (next.isDirectory()) {
                    stack.push(next);
                }
            }
        }
        return files;
    }

    public static void main(String[] args) {
        String path = "/Users/";
        System.out.println(getFileNumber(path));
    }
}
