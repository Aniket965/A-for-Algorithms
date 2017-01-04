
public class InsertionSort {

	public static void main(String[] args){
		/* psuedo data for array */
        int numberOfElements = 6;
        int[] arr = { 2, 10, 8, 1, 4, 1 };
        //call to  selection sort function
        insertionSort(arr, numberOfElements);
		
	}
	static void insertionSort(int[] array,int length){
		 /* loop across the  array */
        for (int i = 1; i < length ; i++)
        {
            /*element to be inserted is selected*/
          
        	
        	int elementToBeInserted=array[i];
        	
        	int j;
        	/*element to be inserted is then arranged in proper place in ordered sub array*/
        	/* loop in ordered sub array finds proper place in array as well as shifts the array for creating proper space*/
        	for (j = i-1;j>=0&&array[j]>elementToBeInserted; j--)
        	{       
                    /* shifts the array one place for creating proper space for element */
                	array[j+1] = array[j];
                
            }
        	/*adds the element in proper space*/
        	array[j+1]=elementToBeInserted;
        }

        //prints sorted array
        System.out.print( "sorted array is ");
        for (int i = 0; i < length; i++)
        {
            /* prints every element of array*/
        	System.out.print(array[i]+" ");
        }
        
        
    }
	
}

