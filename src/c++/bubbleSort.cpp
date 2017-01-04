#include<iostream.h>
void bubbleSort(int array[],int length) {
  /* loop accross the second last array */
for (int i = 0; i < length-1; i++) {
  /* loop across the unsorted subarray*/
  for (int j = 0; j < length-i-1; j++) {
    /* checks if any small number is caught  */
    if (array[j+1]<array[j]) {
      /* swap the digits */
      int temp;
      temp=array[j+1];
      array[j+1]=array[j];
      array[j]=temp;
    }
  }
}

//prints sorted array
cout<<"sorted array is ";
for ( i = 0; i < length; i++) {
  /* prints every element of array*/
  cout<<array[i]<<" ";
}

}
int main() {
  /* psuedo data for array */
  int numberOfElements=6;
  int arr[]={2,10,8,1,4,1};
  //call to  bubble sort function
  bubbleSort(arr,numberOfElements);

    return 0;
}
