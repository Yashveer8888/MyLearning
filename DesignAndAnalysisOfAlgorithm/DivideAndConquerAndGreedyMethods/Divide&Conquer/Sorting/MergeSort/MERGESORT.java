public class MERGESORT {
   static int[] merge(int[] left, int[] right) {
       int[] merged = new int[left.length + right.length];
       int i = 0, j = 0, k = 0;
       while (i < left.length && j < right.length) {
           if (left[i] <= right[j]) {
               merged[k] = left[i];
               i++;
           } else {
               merged[k] = right[j];
               j++;
           }
           k++;
       }
       while (i < left.length) {
           merged[k] = left[i];
           i++;
           k++;
       }
       while (j < right.length) {
           merged[k] = right[j];
           j++;
           k++;
       }
       return merged;
   }

   static int[] MergeSort(int[] arr) {
       if (arr.length <= 1) {
           return arr;
       }
       int mid = arr.length / 2;
       int[] left = new int[mid];
       int[] right = new int[arr.length - mid];
       for (int i = 0; i < mid; i++) {
           left[i] = arr[i];
       }
       for (int j = mid; j < arr.length; j++) {
           right[j - mid] = arr[j];
       }
       return merge(MergeSort(left), MergeSort(right));
   }
   public static void main(String[] args) {
       int[] arr = {50, 1, 7, 6, 2, 9, 77, 1, 0};
       MERGESORT ob = new MERGESORT();
       int[] sortedArray = ob.MergeSort(arr);
       for (int num : sortedArray) {
           System.out.print(num + " ");
       }
   }
}
