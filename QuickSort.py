'''
The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. 
The integer in the ith row of the file gives you the ith entry of an input array.
Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. 
As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m-1 to your running total of comparisons. 
(This is because the pivot element is compared to each of the other m-1 elements in the subarray in this recursive call.)
WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons.
For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).
'''
from random import randint

arr = [9,8,7,10,5,4,11]

with open('QuickSort.txt') as f:
    list = [int(i) for i in f.read().splitlines()]
    
def paritision(arr):

    pivot = arr[0]
    i = 1
    for j in range(1, len(arr)):
        if arr[j] < pivot:
            arr[i], arr[j] =arr[j], arr[i]
            i +=1
    arr[0], arr[i-1] = arr[i-1], arr[0]
    return i-1

    
def QuickSortFirst(arr):

    global count
    if len(arr) <= 1:
        return arr
    count += len(arr)-1
    pivot = paritision(arr)

    return QuickSortFirst(arr[:pivot]) +[pivot] +QuickSortFirst(arr[pivot+1:])

# count = 0
# QuickSortFirst(list)
# print (count)

def QuickSortLast(arr):

    global count
    
    if len(arr) <= 1:
        return arr
    pivot = arr[-1] 
    arr[0],arr[-1]=arr[-1],arr[0]
    
    count += len(arr)-1
    
    pivot = paritision(arr)
    
    return QuickSortLast(arr[:pivot]) +[pivot] +QuickSortLast(arr[pivot+1:])

count = 0
QuickSortLast(list)
print (count)

def QuickSortMedian(arr):

    global count
    
    if len(arr) <= 1:
        return arr
    
    #choose pivot
    if len(arr)%2 == 0:
        ordset = [arr[0],arr[len(arr)//2 - 1], arr[-1]]
    else:
        ordset = [arr[0],arr[len(arr)//2], arr[-1]]
    ordset.sort()
    p = arr.index(ordset[1])
    arr[0], arr[p] = arr[p], arr[0]
    
    count += len(arr)-1
    
    pivot = paritision(arr)
    
    return QuickSortMedian(arr[:pivot]) +[pivot] +QuickSortMedian(arr[pivot+1:])

# count = 0
# QuickSortMedian(list)
# print (count)


# weird enough if I don't comment out the section above for each and let the program output three counts. It doesn't work even though I zero out the count. 

def QuickSortRand(arr):
    
    if len(arr) <= 1:
        return arr

    ri = randint(0,len(arr)-1)
    pivot = arr[ri] 
    arr[0],arr[ri]=arr[ri],arr[0]

    pivot = paritision(arr)
    
    return QuickSortRand(arr[:pivot]) +[pivot] + QuickSortRand(arr[pivot+1:])


        
    