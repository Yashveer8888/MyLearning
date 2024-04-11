public class QUICKSORT {
   static int Partition(int []arr){
      int pivot=arr[arr.length-1];
      int p=0;
      for(int i=0;i<arr.length-1;i++){
         int temp=arr[p];
         arr[p]=arr[i];
         arr[i]=temp;
         p++;
      }
      int temp=pivot;
      pivot=arr[p];
      arr[p]=temp;
      return p;
   }
   static int [] QuickSort(int []arr){
      if(arr.length<=1){
         return arr;
      }
      int p=Partition(arr);
      int[] less = new int[p];
      int[] greater = new int[arr.length - p-1];
      for (int i = 0; i < p; i++) {
        less[i] = arr[i];
      }
      QuickSort(less);
      for (int j = p+1; j < arr.length; j++) {
         greater[j - p+1] = arr[j];
      }
      QuickSort(greater);
      int [] array =new int[less.length+greater.length];
      for(int i=0;i<array.length;i++){
         int c=0;
         for (int j = 0; j < p; j++) {
            array[c] = arr[j];
            c++;
         }
         for (int j = 0; j < p; j++) {
            array[c] = arr[j];
            c++;
         }
      }
   return array;
   }
   public static void main(String[] args) {
      int[] arr = {50, 1, 7, 6, 2, 9, 77, 1, 0};
       QUICKSORT ob = new QUICKSORT();
       int[] sortedArray = ob.QuickSort(arr);
       for (int num : sortedArray) {
           System.out.print(num + " ");
       }
   }
 
}