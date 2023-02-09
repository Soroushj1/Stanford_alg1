from random import randint

arr = [9,8,100,91,95,80,50,30,45,40]


def partision(arr, p):
    
    if len(arr)>0:
        pivot = arr[p] 
        arr[0],arr[p]=arr[p],arr[0]
    
    if len(arr)<2 or not pivot:
        return arr, arr[0]
    
    i = 1
    for j in range(1, len(arr)):
        if arr[j] < pivot:
            arr[i], arr[j] =arr[j], arr[i]
            i +=1
    arr[0], arr[i-1] = arr[i-1], arr[0]

    return arr, i-1


def rselect(arr, number):
    
    if len(arr)>1:
        p = randint(0, len(arr)-1)
        arr, p = partision(arr, p)
        
        if number < arr[p]: 
            return rselect(arr[:p], number)
        elif number> arr[p]:
            return rselect(arr[p+1:], number)
        else:
            return arr[p]
    else:
        return arr[0]

print(rselect(arr, 30))

    