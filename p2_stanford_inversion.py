with open('p2_stanford_file.txt') as f:
    lines = [int(i) for i in f.read().splitlines()]

a = [10, 2, 1, 5, 5, 2, 11]


def countInversion(array):
    if len(array) <= 1:
        return array, 0 
    
    mid = len(array)//2
    leftHalf = array[:mid]
    rightHalf = array[mid:]
    sortedLeft, leftCount  = countInversion(leftHalf)
    sortedRight, rightCount =  countInversion(rightHalf)
    sortedAll, crossCount= crossCounter(sortedLeft, sortedRight)
    finalCount = leftCount + rightCount + crossCount
    return sortedAll, finalCount
    
def crossCounter(leftHalf,rightHalf):
    sortedArray = []
    i=j=count=0
    while i<len(leftHalf) and j<len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray.append(leftHalf[i])
            i += 1
        else:
            sortedArray.append(rightHalf[j])
            count += len(leftHalf)-i
            j += 1
    while i< len(leftHalf): 
        sortedArray.append(leftHalf[i])
        i += 1
    while j<len(rightHalf):
        sortedArray.append(rightHalf[j])
        j +=1
    return sortedArray, count

print(countInversion(a))
#countInversion(lines)
    