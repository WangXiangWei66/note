package Class05;


//import javax.xml.bind.DatatypeConverter;//将字节数字转化为16进制字符串
import java.security.MessageDigest;//计算哈希值的核心类
import java.security.NoSuchAlgorithmException;//使用的哈希算法不存在时会抛出异常
import java.security.Security;

public class Hash {
    private MessageDigest hash;//存储哈希算法的实例

    public Hash(String algorithm) {//传入要使用的哈希算法
        try {
            hash = MessageDigest.getInstance(algorithm);//获取指定算法的Message实例
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();//如果算法不存在，会打印异常堆栈信息
        }
    }

//    public String hashCode(String input) {
//        return DatatypeConverter.printHexBinary(hash.digest(input.getBytes())).toUpperCase();//先将输入的字符串转化为字节数组，然后计算哈希值，然后将字节数组转化为十六进制字符串，再将十六进制转化为大写
//    }
    public static void main(String[]args){
        System.out.println("支持的算法:");
        for(String str : Security.getAlgorithms("MessageDigest")){
            System.out.println(str);//java.security为java安全框架提供了多种安全相关的方法和功能,getAlgorithm为了接受字符串参数，这个参数代表服务类型
        }
        System.out.println("=========");

        String algorithm = "SHA-256";
        Hash hash = new Hash(algorithm);

        String input1 = "zuochengyunzuochengyun1";
        String input2 = "zuochengyunzuochengyun2";
        String input3 = "zuochengyunzuochengyun3";
        String input4 = "zuochengyunzuochengyun4";
        String input5 = "zuochengyunzuochengyun5";
//        System.out.println(hash.hashCode(input1));
//        System.out.println(hash.hashCode(input2));
//        System.out.println(hash.hashCode(input3));
//        System.out.println(hash.hashCode(input4));
//        System.out.println(hash.hashCode(input5));
    }
}
