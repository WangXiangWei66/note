package class01;

import java.util.Arrays;


public class Code04_SelectionSort {

     public static void selectionSort(int [] arr){
         if (arr==null ||arr.length<2){
             return;
         }
         for (int i=0;i< arr.length-1;i++){
             int minIndex=i;
             for(int j=i+1;j<arr.length;j++){
                 if(arr[j]<arr[minIndex]){
                     minIndex=j;
                 }
             }
             swap(arr,i,minIndex);
         }
     }

     public static void swap(int [] arr,int i, int j){
         int tmp=arr[j];
         arr[j]=arr[i];
         arr[i]=tmp;
     }

     //for test
public static void comparator(int[]arr){
    Arrays.sort(arr);
}

    public static int[] generateRandomArray(int maxSize , int maxValue){
         //Math.random()   [0,1)
        //Math.random()*N  [0,N)
        //(int)(Math.random()*N)  [0,N-1]
        int[] arr =new int [(int) ((maxSize+1)*Math.random())];
        for(int i=0;i<arr.length;i++){
            //[-?,?]
            arr[i] = (int) ((maxSize+1)*Math.random())-(int)(maxValue*Math.random());
        }
        return arr;
     }
     //for test
   public static int[] copyArray(int[] arr){
         if(arr==null){
             return  null;
         }
         int []ans=new int[arr.length];
         for(int i =0; i< arr.length;i++){
             ans[i]=arr[i];
         }
         return ans;
   }

   //for test
   public static boolean isEqual(int[]arr1,int[]arr2){
         if((arr1 == null &&arr2 !=null)||(arr1 != null &&arr2 == null)){
             return  false;
       }
       if(arr1 ==null && arr2 == null){
           return true;
       }
       if(arr1.length != arr2.length){
           return false;
       }
       for(int i =0;i< arr1.length; i++){
           if(arr1[i] != arr2[i]){
               return false;
           }
       }
       return true;
   }

   //for test
    public static void printArray(int[] arr){
         if(arr==null){
             return;
         }
         for( int i=0;i<arr.length;i++){
             System.out.print(arr[i]+" ");
         }
         System.out.println();
    }

   //for test

    public static void main(String[] args){
         int testTime=500000;
         int maxSize=100;
         int maxValue=100;
         boolean succeed=true;
         for(int i=0;i<testTime;i++){
             int[]arr1=generateRandomArray(maxSize,maxValue);
             int[]arr2=copyArray(arr1);
             selectionSort(arr1);
             comparator(arr2);
             if(!isEqual(arr1,arr2)) {
                 succeed = false;
                 printArray(arr1);
                 printArray(arr2);
                 break;
             }
         }
         System.out.println(succeed ?"Nice!" : "Fucking Fucked" );

         int[] arr=generateRandomArray(maxSize,maxValue);
         printArray(arr);
         selectionSort(arr);
         printArray(arr);
    }
}
