import heapq
from functools import reduce



def file_reader():
    for row in open("median.txt", "r", encoding="utf-8"):
        yield int(row.split('\n')[0])

def add(input, heap, bool= True):
    if bool:
        heapq.heappush(heap, input)
    else: 
        heapq.heappush(heap, input * -1)
        
        
def pop(heap, bool=True):
    if bool:
        return heapq.heappop(heap)
    else:
        return heapq.heappop(heap)*-1

def findMedian(minHeap, maxHeap, new_input):

    median = 0
    add(new_input, maxHeap, False)

    # conditions for balancing 
    
    if minHeap and maxHeap and -1 * maxHeap[0] > minHeap[0]:
        add(pop(maxHeap,False), minHeap)
    if len(minHeap) - len(maxHeap) > 1:
        add(pop(minHeap), maxHeap, False)
    if len(maxHeap) - len(minHeap)> 1:
        add(pop(maxHeap, False),minHeap)
        
    # conditions for finding the median
        
    if len(maxHeap) == len(minHeap): 
        # median = (minHeap[0]+ maxHeap[0]* -1)/2
        median = (-1*maxHeap[0]) # to satisfy the definition of median in the assignment. 
    elif len(maxHeap) > len(minHeap):
        median = -1* maxHeap[0]
    else:
        median = minHeap[0]
    return median



class node:
    
    def __init__(self, value):
        
        self.value = value
        self.left = None
        self.right = None


class BST:
    
    def __init__(self, root):
        self.root = root
        
    def add(self, value):
        
        curr = self.root
        while value < curr.value:    
            if curr.left:
                curr = curr.left
            else:
                curr.left = node(value)
                break
        while value > curr.value:
            if curr.right:
                curr = curr.right
            else:
                curr.right = node(value)
                break
    
    def min_max(self):
        
        min = 1e10 
        max = 0
        curr = self.root
        while curr.left: 
            curr = curr.left
        else:
            min = curr.value
            
        curr = self.root
        while curr.right:
            curr = curr.right
        else:
            max = curr.value
        return min, max
    
            
    def in_order_traversal(self):
        
        # NOT COMPLETED: to implement in order traversal
        pass
            
    
    

def main():

    med = []
    
    new_bst = BST(node(5))
    new_bst.add(6)
    new_bst.add(7)
    new_bst.add(2)
    new_bst.add(3)
    new_bst.min_max()
    new_bst.in_order_traversal()
    
    
    
    
    minHeap = [] # gives the min of the upper half
    maxHeap = [] # gives the max of the lower half
    row = file_reader()
    for new_input in row: 
        med.append(findMedian(minHeap, maxHeap, new_input))
        sum = reduce(lambda x, y: x+y, med)
    print(sum)
    return sum % 10000
    

if __name__=="__main__":
    main()                 