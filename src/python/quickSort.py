#quick sort algorithm in python

## function for making partition
def partition(list ,startingIndex,endingIndex):
    #pivot is selected element to which we have to compare elements
    pivot= list[endingIndex]
    #partitionLine is the index of partitionLine
    partitionLine=startingIndex
    #loop for across list
    for i in range(startingIndex,endingIndex):
        #checks if any small element is caught then pivot
        if list[i] <= pivot:
            #if small elemen is found partionLine element is changed with it
            list[partitionLine],list[i]=list[i],list[partitionLine]
            #moves the partionLine one index ahead
            partitionLine=partitionLine+1
    #after loop pivot is placed at partitionLine
    list[partitionLine],list[endingIndex]=list[endingIndex],list[partitionLine]
    #index of partionLine is returned
    return partitionLine

#function that calls the function partition
#divides the list into 2 sublist with ignoring partion line
def quickSort(list,startingIndex,endingIndex):
        if startingIndex < endingIndex:
            #calls the partition function
            partitionLine=partition(list ,startingIndex,endingIndex)
            #divides list into 2 sublist then calls the itself
            quickSort(list,startingIndex,partitionLine-1)
            quickSort(list,partitionLine+1,endingIndex)



##psuedo data for list
list=[2,10,8,1,4,1,234,4,23,5,5,436,0,7,7,8,678,768]
#calls the quickSort function with length of list and list
quickSort(list,0,len(list)-1)
#prints the sorted lists
print(list)
