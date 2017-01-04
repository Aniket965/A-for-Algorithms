//shellSortfunction
function shellSort(array) {
var gap;
//gap is taken of size half of array length
/*loop for reducing  gap size one bye one to with minimum value of 1*/
for (gap =Math.floor(array.length/2+1); gap >= 1; gap--) {
/*loops for changing the swaping values with gap size*/
for (var i = 0; i <= array.length-gap; i++) {
  /*checks if elements needed to be swapped*/
  if(array[i]>array[i+gap]){
/*swaps the digits using temproray variable*/
  var  temp=array[i+gap];
    array[i+gap]=array[i];
    array[i]=temp;
  }
}
}
/*prints the sorted  array*/
console.log('the sorted array is '+array);
}
/* psuedo data for array */
var arr=[ 2, 10, 8, 1, 4, 1,13,2,14,5,56,1 ,4,15,23,213,412,4,432,2];
/*calls to  shell sort function*/
shellSort(arr);
