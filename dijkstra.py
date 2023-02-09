from collections import defaultdict
import math

class Heap:
    
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.heap_arr = []
        self.heap_size = capacity
        self.heap_map = defaultdict(int) # gives value: index of heap_arr
    
    def populate_heap(self, capacity,src):
        #everything except the src gets a value of infinity in the initial heap
        inf = 1e7
        for i in range(1,capacity+1):
            if i != src:
                self.heap_arr.append([i,inf])
                self.heap_map[i] = i-1
            else:
                self.heap_arr.append([i,0])
                self.heap_map[i] = i-1
    
    def bubble_down(self, index):
        while not self.get_left(index)[1] == None:
            small, small_index = self.get_left(index)  # assuming the left is smaller
            if not self.get_right(index)[0] == None and self.get_right(index)[0][1]< self.get_left(index)[0][1]: # correcting the above assumption
                small, small_index = self.get_right(index)
            if small[1] >=  self.heap_arr[index][1]:
                break
            else:
                self.heap_arr[index], self.heap_arr[small_index] = self.heap_arr[small_index], self.heap_arr[index]
                self.heap_map[self.heap_arr[small_index][0]], self.heap_map[small[0]] = small_index, index
            index = small_index
        
    def bubble_up(self,index):
        while not self.get_parent(index)[1] == None: #this could be zero therefore, I can't simply do "while self.get_parent(index)[1]:"
            small , small_index= self.get_parent(index) # assuming the parent is smaller
            if small[1] <= self.heap_arr[index][1]:
                break
            else: 
                self.heap_arr[index], self.heap_arr[small_index] = self.heap_arr[small_index], self.heap_arr[index]
                self.heap_map[self.heap_arr[small_index][0]], self.heap_map[small[0]] = small_index, index
            index = small_index
    
    # Peaks at the top which in this case in the case of minHeap is the minimum
    # and then calls bubble_down to keep the heapify invariant
    def peak(self):
        if self.heap_size:
            data = self.heap_arr[0]
            last = self.heap_arr[-1]
            self.heap_arr[-1], self.heap_arr[0] = self.heap_arr[0], self.heap_arr[-1] 
            self.heap_map[last[0]], self.heap_map[data[0]] = 0, len(self.heap_arr)-1
            self.heap_arr.pop()
            self.heap_map.pop(data[0])
            self.heap_size = len(self.heap_arr)
            self.bubble_down(0)
            return data  # the output is an array [node number, distance]
        else:
            raise("empty heap")
        
    def insert(self, v):
        self.heap_arr.append(v)
        self.heap_size = len(self.heap_arr)
        self.heap_map[v[0]] = self.heap_size-1
        self.bubble_up(self.heap_size-1)
    
    
    def remove(self, v):
        if self.heap_size:
            data = self.heap_arr[v]
            last = self.heap_arr[-1]
            self.heap_arr[-1], self.heap_arr[v] = self.heap_arr[v], self.heap_arr[-1] 
            self.heap_map[last[0]], self.heap_map[data[0]] = v, len(self.heap_arr)-1
            self.heap_arr.pop()
            self.heap_map.pop(data[0])
            self.heap_size -=1
            #does popping the array change heap_map values. 
            if v == self.heap_size:
                return data
            else:
                if self.get_parent(v)[1] == None or self.get_parent(v)[0][1] <= self.heap_arr[v][1]:
                    self.bubble_down(v)
                else:
                    self.bubble_up(v)

    
    def get_left(self,index):
        l = 2*index + 1
        return (self.heap_arr[l], l) if l < self.heap_size else (None,None)
    
    def get_right(self,index):
        r = 2*index +2
        return (self.heap_arr[r], r) if r < self.heap_size else (None,None)
    
    def get_parent(self,index):
        p = (index - 1)//2
        return (self.heap_arr[p],p) if p >= 0 else (None, None)
    
    
class Graph:
    
    def __init__(self, size):
         self.size = size
         self.graph = defaultdict(list)
         
    def add_edges(self,arr):
        for i, node in enumerate(arr,start=1): 
            for j, adj in enumerate(node):
                if j == 0:
                    continue
                else:
                    self.graph[i].append(adj)

    def dijkstra(self,src):
        
        distance = defaultdict(list)
        path = []
        minHeap = Heap(self.size)
        minHeap.populate_heap(minHeap.capacity,src)
        
        while minHeap.heap_arr:
            index , dist = minHeap.peak()
            distance[index] = dist
            path.append([index,dist])
            for neighbor in self.graph[index]:
                if neighbor[0] not in distance:
                    old_dijkstra_greedy_score = minHeap.heap_arr[minHeap.heap_map[neighbor[0]]][1]
                    minHeap.remove(minHeap.heap_map[neighbor[0]])
                    new_dijkstra_greedy_score=  min(old_dijkstra_greedy_score, dist + neighbor[1])
                    minHeap.insert([neighbor[0], new_dijkstra_greedy_score])
        
        return distance, path
            # for j in range(len(minHeap.heap_arr)):
            #     for i in self.graph[index]: # looking at all the adjacent nodes
            #         if i[0] == minHeap.heap_arr[j][0]:
            #             temp = minHeap.heap_arr[j][0]
            #             minHeap.remove(j)
            #             new_dijkstra_greedy_score=  dist + i[1]
            #             minHeap.insert([temp, new_dijkstra_greedy_score])

        
    
    
def main():
    with open("dijkstra.txt", "r", encoding="utf-8") as file: 
        nodes = file.read().strip().splitlines()
        arr = [[]  for i in range(len(nodes))]
        for i in range(len(nodes)-1):
            for elem in nodes[i].strip().split("\t"):
                arr[i].append([int(i) for i in elem.split(",")])
        graph = Graph(len(nodes))
        graph.add_edges(arr)
        distance,path = graph.dijkstra(1)
        print(distance[7],distance[37],distance[59],distance[82],distance[99],distance[115],distance[133],distance[165],distance[188],distance[197])
        # answer to assignment: 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068    
if __name__ == "__main__":
   main()