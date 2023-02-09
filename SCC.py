from collections import deque
from itertools import islice
import os
import sys
import threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)



class Node:
    
    def __init__(self, val, edges=[]) -> None:
        self.val = val
        self.edges = edges or [] # list of all the nodes
        self.visited = False
        
class Graph:
    
    def __init__(self):
        self.nodes = {}
        self.trans= None
        
    def populate_graph(self, file):
        file= file.splitlines()
        for edge in file:
            edge = edge.strip().split(" ")             
            for i in range(len(edge)):
                if i == 0:
                    t=int(edge[i])
                    self.nodes[t] = self.nodes[t] if t in self.nodes.keys() else self.create_node(t) 
                else:
                    h =int(edge[i])
                    self.nodes[h] = self.nodes[h] if h in self.nodes.keys() else self.create_node(h) 
                    self.nodes[t].edges.append(self.nodes[h])
    
    def transpose(self, file):
        Gr = Graph()
        file= file.splitlines()
        for edge in file:
            edge = edge.strip().split(" ")             
            for i in range(len(edge)):
                if i == 0:
                    h=int(edge[i])
                    Gr.nodes[h] = Gr.nodes[h] if h in Gr.nodes.keys() else self.create_node(h) 
                else:
                    t =int(edge[i])
                    Gr.nodes[t] = Gr.nodes[t] if t in Gr.nodes.keys() else self.create_node(t) 
                    Gr.nodes[t].edges.append(Gr.nodes[h])
        self.trans = Gr
    
    
    def create_node(self, node_value):
        new_node = Node(node_value)
        return new_node
    
        
    #Using DFS_recursive algorithm to calculate fininshing times with topological sorting.
    def finishing_time_rec(self, start_node_value, ftime):
        start_node = self.trans.nodes[start_node_value]
        if start_node.visited == True or not start_node.edges:
            start_node.visited = True
            ftime.append(start_node_value)
            return ftime
        else:
            start_node.visited = True
            for edge in start_node.edges:
                if not edge.visited:
                    ftime =self.finishing_time_rec(edge.val, ftime)
            ftime.append(start_node_value)
        return ftime
    
    def dfs_sec(self, start_node_value):
        closed = set()
        start_node = self.nodes[start_node_value]
        to_visit = deque([start_node])
        while to_visit:
            node = to_visit.pop()
            closed.add(node.val)
            node.visited = True
            not_seen=[edge for edge in node.edges if edge.visited == False ]
            to_visit.extend(not_seen)
        return closed


    def dfs_loop(self):
        global val
        ftime = []
        for j in range(len(self.trans.nodes)-1, 0,-1):
            if not self.trans.nodes[j].visited:
                val = self.trans.nodes[j].val
                ftime= self.finishing_time_rec(val,ftime)
                
        self._clear_nodes()
        components = []
        for i in range(len(ftime)-1,-1,-1):
            node = self.nodes[ftime[i]]
            if not node.visited:
                node.visited = True
                closed = self.dfs_sec(node.val)
                components.append(closed)
                sizes = [len(i) for i in components]
        sizes = sorted(sizes,reverse=True)[0:5]
        return sizes
    
    def _clear_nodes(self):
        for nodes in self.nodes.values():
            nodes.visited = False

def main():
    
    with open("SCC.txt", "r", encoding="utf-8") as file:
        # arr =   [[int(nodes) for nodes in row.strip().split(" ")] for row in file.read(100).strip().split("\n")]
        # file = list(islice(file, 100))
        # new_graph = Graph(file)
        arr = file.read()
        new_graph = Graph()
        new_graph.populate_graph(arr)
        new_graph.transpose(arr)
        print(new_graph.dfs_loop())
        # output = [434821, 968, 459, 313, 211]
        
if __name__ == "__main__":
    main()
    
