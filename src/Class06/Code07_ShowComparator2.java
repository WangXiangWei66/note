package Class06;

import javax.accessibility.AccessibleRelationSet;
import javax.lang.model.util.AbstractElementVisitor14;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.function.IntToDoubleFunction;

public class Code07_ShowComparator2 {
    public static class MyComparator implements Comparator<Integer>{
        //负，第一个参数在前
        //正，第二个参数在前
        //0，谁放前都行
        @Override
        public int compare(Integer o1, Integer o2) {
            if(o1<o2){
                return 1;
            }else if(o1>02){
                return -1;
            }
            else{
                return 0;
            }
        }
    }
    public static class Student{
        public String name;
        public int id;
        public int age;
        public Student(String name, int id, int age){
            this.name=name;
            this.id=id;
            this.age=age;
        }
    }
    //谁id大，谁放前
    public static class Idcomparator implements Comparator<Student>{
        //如果返回负数，则认为第一个参数排在前面
        //如果返回正数，则认为第二个参数排在前面
        //如果返回0，认为谁放前面无所谓

        @Override
        public int compare(Student o1, Student o2) {
            if(o1.id< o2.id){
                return 1;
            }else if(o1.id>o2.id){
                return -1;
            }else{
                return 0;
            }
        }
    }
    public static void main(String[]args){
        String str1="abc";
        String str2="b";
        System.out.println(str1.compareTo(str2));
        PriorityQueue<Student> heap=new PriorityQueue<>(new Idcomparator());
       Student s1 = new Student("张三", 6, 27);
        Student s2 = new Student("李四", 4, 17);
        Student s3 = new Student("王五", 3, 29);
        Student s4 = new Student("赵六", 1, 9);
        Student s5 = new Student("左七", 7, 34);
        heap.add(s1);
        heap.add(s2);
        heap.add(s3);
        heap.add(s4);
        heap.add(s5);
        System.out.println("========");
        while(!heap.isEmpty()){
            Student s = heap.poll();
            System.out.println(s.name+","+s.id+","+s.age);
        }
    }
}
