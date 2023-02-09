array = [5, 3,8,9,1,7,0,2,6,4]
print(array)
def mergeSort(array):
    #base case is when the array is length 1
    if len(array) ==1:
        return array
    
    mid = len(array)//2
    right = array[mid:]
    left = array[:mid]
    print(f"left >>> {left}, right >> {right}")
    mergeSort(left)
    mergeSort(right)
    i=j=k= 0
    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            #Its super super important that the array that is fed into the function
            # is being dynamically changed using the returned sorted arrays from the recursive calls!!!
            # for example given array [7,0, 2,6,4], the recursive calls have so far returned [0,7] and [2,4,6] sorted arrays. 
            # then here first comparison looks at left[0] = 0 and right[0]=2 and picks 0.
            # the second comparison looks at left[1]=7 and right[0]=2 and picks 2. So far we got [0,2,and the rest of the original array]
            # the third comparison looks at left[1]=7 and right[1]=4 and picks 4.
            # the fourth comparison looks at left[1]=7 and right[2]=6 and picks 6. 
            # now j=3<len(right)=3 does not hold anymore. We have so far [0,2,4,6, and the rest of the original array]
            array[k] = left[i]
            i += 1   
        else:
            array[k] = right[j]
            j += 1
        k +=1
    while i<len(left):
        #This while loop is where we are picking the rest of the array. 
        # In our case i=1<len(left)=2 so we pick the rest of the left array in this case only left[1]=7.
        array[k] = left[i]
        i += 1
        k += 1
    while j<len(right):

        array[k]= right[j]
        j  += 1
        k += 1
    print (array)
            
mergeSort(array)

print(array)