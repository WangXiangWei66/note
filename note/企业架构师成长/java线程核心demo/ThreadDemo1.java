//java线程示例代码
//继承了Java的Thread类，即这是一个自定义线程类
public class ThreadDemo1 extends Thread {

    @Override//注解，告诉编译器下面的run方法是重写父类的方法，如果拼写错误，或者参数不匹配，编译器会报错

    public void run() {
        //try块，用来捕获可能出现的异常
        try {
            Thread.sleep(2000);
            //Thread.currentThread().getName()：获取当前线程的名称
            System.out.println(Thread.currentThread().getName() + " my thread");

        } catch (InterruptedException e) {
            //打印异常堆栈信息，帮助调试线程终端的原因
            e.printStackTrace();
        }
    }
}

