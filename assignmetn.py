#Complete code for insertion, quicksort and merge sort algorithms
#we have included the comparision counter operations
#The code takes all tyes of required inputs

import numpy
import time

#inseriton sort
print("INSERTION SORT")
def insertionSort(array):
    
    start = time.time()
    count = 0
    
    for step in range(1, len(array)):
        value = array[step]
        j = step - 1
        
        while  value < array[j] and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
            count += 1
        
        array[j + 1] = value
        
    print("number of comparision operations performed: ", count)
    end = time.time()
    timeTaken = end - start
    print("\ntime taken to complete the sorting: ", timeTaken)
    print('\nSorted Array in Ascending Order:')
    print(data)
    
 #for random numbers data
print("FOR RANDOM NUMBERS INPUT")
data = numpy.random.randint(low = 0, high = 10000, size = 10000)
insertionSort(data)

  # for ascending order data
print("\n\nFOR ASCENDING ORDER INPUT")
data = [ i for i in range(10000)]
insertionSort(data)

#for descending order data
print("\n\nFOR DESCENDIG ORDER INPUT")
data = [ i for i in range(10000, 0, -1)]
insertionSort(data)

#for few items
print("\n\nFOR FEW ITEMS")
data = [ 4, 7, 9, 1, 0, 4, 8, 12, 44]
insertionSort(data)

#quicksort
print("\n\nQUICKSORT")
count_ass = 0
count_compa =0
count_return = 0
start = time.time()
def dividing(array,firstIndex,lastIndex):
    global count_ass, count_compa
    pointer = ( firstIndex- 1 )
    pivot= array[lastIndex]
    count_ass += 2
 
    for i in range(firstIndex, lastIndex):
        if   array[i] <= pivot:
 
            pointer += 1
            array[pointer],array[i] = array[i],array[pointer]
            count_ass += 3
            count_compa += 1
 
    array[pointer+1],array[lastIndex] = array[lastIndex],array[pointer+1]
    count_ass += 2
    return (pointer+1)
 

def quickSort(array,firstIndex,lastIndex):
    global count_ass, count_compa
    
    stack = [0] * (lastIndex - firstIndex + 1)
    top = 0
    stack[top] = firstIndex
    top = top + 1
    stack[top] = lastIndex
    count_ass += 5
   
    while top >= 0:
 
        count_compa += 1
        lastIndex = stack[top]
        top = top - 1
        firstIndex = stack[top]
        top = top - 1
 
        count_ass += 4
        p = dividing( data, firstIndex, lastIndex)
        

        
        if p-1 > firstIndex:
            top = top + 1
            stack[top] = firstIndex
            top = top + 1
            stack[top] = p - 1
            count_compa += 1

        
        if p+1 < lastIndex:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = lastIndex
            count_compa += 1

    
    print("number of operation", count_compa + count_ass )
    end = time.time()
    timeTaken = end - start
    print("\ntime taken to complete the sorting: ", timeTaken)
    print('\nSorted Array in Ascending Order:')
    print(data)
    
 #for random numbers data
print("\nFOR RANDOM NUMBERS INPUT")
data = numpy.random.randint(low = 0, high = 10000, size = 10000)
n = len(data)
quickSort(data, 0, n-1)

  # for ascending order data
print("\n\nFOR ASCENDING ORDER INPUT")
data = [ i for i in range(10000)]
n = len(data)
quickSort(data, 0, n-1)


#for descending order data
print("\n\nFOR DESCENDIG ORDER INPUT")

data = [ i for i in range(10000, 0, -1)]
n = len(data)
quickSort(data, 0, n-1)

#for few items
print("\n\nFOR FEW ITEMS")
data = [ 4, 7, 9, 1, 0, 4, 8, 12, 44]
n = len(data)
quickSort(data, 0, n-1)


#merge sort
print("\n\nMERGE SORT")
count_ass = 0  
count_compa = 0
start = time.time()
def mergeSort(array):
    global count_ass, count_compa
   
    if len(array) > 1:
        count_compa += 1
        mid = len(array) // 2
        leftarray = array[:mid]
        rightarray = array[mid:]
       
        # Recursive call when we go two list (left and right) for sorting
        mergeSort(leftarray)
        mergeSort(rightarray)

        # Because we have two lists, so we need to iterators for iteration of each list
        m = 0
        n = 0
        # We need one common iterator which iterates to the main list
        z = 0
        count_ass+=3

        while m < len(leftarray) and n < len(rightarray):
            if leftarray[m] <= rightarray[n]:
              # Here we are using the first left side elements
              array[z] = leftarray[m]
              # Increment the main iterator
              m += 1
              count_ass+=2
                    
            else:
                array[z] = rightarray[n]
                n += 1
                count_ass+=2
                    
            z += 1
            count_ass+=1
            count_compa += 2
                

        # If values are left in the list, then we process here
        while m < len(leftarray):
            array[z] = leftarray[m]
            m += 1
            z += 1
            count_ass+=3
            count_compa += 1

        while n < len(rightarray):
            array[z]=rightarray[n]
            n += 1
            z += 1
            count_ass+=3
            count_compa += 1
   
 #for random numbers data
print("\n\nFOR RANDOM NUMBERS INPUT")
data = numpy.random.randint(low = 0, high = 10000, size = 10000)
mergeSort(data)
end = time.time()
timeTaken = end - start
print("\ntime taken to complete the sorting: ", timeTaken)
print("number of operation", count_compa + count_ass )
print('\nSorted Array in Ascending Order:')
print(data)

 # for ascending order data
print("\n\nFOR ASCENDING ORDER INPUT")
data = [ i for i in range(10000)]
mergeSort(data)
end = time.time()
timeTaken = end - start
print("\ntime taken to complete the sorting: ", timeTaken)
print("number of operation", count_compa + count_ass )
print('\nSorted Array in Ascending Order:')
print(data)


#for descending order data
print("\n\nFOR DESCENDIG ORDER INPUT")
data = [ i for i in range(10000, 0, -1)]
mergeSort(data)
end = time.time()
timeTaken = end - start
print("\ntime taken to complete the sorting: ", timeTaken)
print("number of operation", count_compa + count_ass )
print('\nSorted Array in Ascending Order:')
print(data)

  
#for few items
print("\n\nFOR FEW ITEMS")
data = [ 4, 7, 9, 1, 0, 4, 8, 12, 44]
mergeSort(data)
end = time.time()
timeTaken = end - start
print("\ntime taken to complete the sorting: ", timeTaken)
print("number of operation", count_compa + count_ass )
print('\nSorted Array in Ascending Order:')
print(data)






















    





