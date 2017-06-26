package Median;
import java.util.*;
// Extra credit: The Bucket Challenge
/*Answer is tehcniclay we can never empty the bucket. 
It will be infinite amount time.
Bigger the bucket the more time it will take.
However, I feel it will be done in 2 hours. 
But reality is that it we can never empty it cause of the water will be in the bucket. 
*/
public class Median {
	public static int find_median(int [] a){
		Arrays.sort(a);
		int size = a.length;
		int m = size/2;
		if (size  %2 == 0){
			return a[m];
		}
		else {
			return (a[m+1] +a[m]) /2;	
		}
	}
	private static int[] generateArray(int i) {
		// TODO Auto-generated method stub
		int [] array = new int[ i];
		Random rand = new Random();
		for (int j =0; j<array.length;j++){
			array[j]=rand.nextInt();
		}
		return array;
	}
	public static String toString (int [] a){
		String t = "[";
		for (int i=  0; i < a.length; i++)
			t += " " + a[i];
		t += "]";
		return t;
	}
	private static int partition(int a[], int start, int end, int pivot)
	{
		int value = a[pivot];
		swap(a,pivot,end);
		int val = start;
		for (int i = start; i < end; i++){
			if ((a[i])<=(value))
			{
				swap(a,i,val);
				val++;
			}	
		}
		swap(a,end,val);
		return val;	
	}
	private static void swap(int [] a, int i, int j){
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;	
	}
//
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// answer will be 23.
		//int a[] = { 3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29};
		int arraySize = 100000;
		int [] test = generateArray(arraySize);
		System.out.println("Median for array of size of 100000: "  + find_median(test) + ".");
	}

}
