/*selection sort*/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SelectionSort
{
    class Program
    {
       static void Main()
        {
            /* psuedo data for array */
            int numberOfElements = 6;
            int[] arr = { 2, 10, 8, 1, 4, 1 };
            //call to  selection sort function
            selectionSort(arr, numberOfElements);

            
        }
        static  void selectionSort(int[] array, int length) {
            /* loop accross the  array */
            for (int i = 0; i < length-1 ; i++)
            {
                /* loop across the unsorted subarray*/
                for (int j = i+1; j < length; j++)
                {
                    /* checks if any small number is than last place of already sorted sub array  */
                    if (array[j] < array[i])
                    {
                        /*adds that to last place of already sorted sub array*/
                        /* swap the digits */
                        int temp;
                        temp = array[j];
                        array[j] = array[i];
                        array[i] = temp;
                    }
                }
            }

            //prints sorted array
            Console.Write( "sorted array is ");
            for (int i = 0; i < length; i++)
            {
                /* prints every element of array*/
                Console.Write(array[i]+" ");
            }
               //added so that program display output untill user press key
            Console.ReadKey();
        }
    

    }
}
