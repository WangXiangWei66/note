package class01;

public class Code01_PrintBinary {
    public static void print(int num){
        for(int i = 31 ; i >= 0 ; i--){
            System.out.print((num & (1 << i)) == 0 ? "0" : "1");
        }
        System.out.println();
    }
    public static void main(String[] args){
        //32位
//        int sum=4;
//        print(sum);
//        int test=1123123;
//        print(test);
//        print(test<<1);
//        print(test<<2);
//        print(test<<8);
//        int a=Integer.MAX_VALUE;
//        System.out.println(a);
//
//        print(-1);

//        int a=Integer.MIN_VALUE;
//        print(a);
////
//        int b=123823138;
//        int c=~b;
//        print(b);
//        print(c);

//        print(-5);

        System.out.println(Integer.MIN_VALUE);
//        System.out.println(Integer.MAX_VALUE);

        int a=12319283;
        int b=3819283;
        print(a);
        print(b);
//        System.out.println("=========");
//        print(a|b);//有一个位置是1，结果便是一
//        print(a&b);//两个数相同时 才会出现1
//        print(a^b);//相同为0，不同为1

//        int a=Integer.MIN_VALUE;
//        print(a);
//        print(a>>1);//移动符号位的同时 符号位不发生变化
//        print(a>>>1);//移动符号位
//

//        int c=Integer.MIN_VALUE;
//        int d=-c;
//
//        print(c);
//        print(d);
    }
}
