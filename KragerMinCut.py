import copy
from random import randint
import math
import multiprocessing
import numpy as np


    
def pickRandEdge(graph):
    u_index = randint(0, len(graph)-1)
    v_index = graph[u_index][randint(1, len(graph[u_index])-1)]
    for i in range(len(graph)):
        if graph[i][0] == v_index:
            v_index = i 
            break
    return u_index, v_index
    
def removeSelfLoop(graph,u):
    i = 1

    while len(graph[u])>i:
        if graph[u][i] == graph[u][0]:
            graph[u].pop(i)
        else:
            i +=1
    return graph

def randContraction(graph, u_index, v_index):
    u = graph[u_index][0]
    v = graph[v_index][0]
    graph[u_index].extend(graph[v_index][1:])
    graph.pop(v_index)
    for i in range(len(graph)):
        if graph[i][0] == u:
            u_index = i
        for j in range(len(graph[i])):
            if graph[i][j] == v:
                graph[i][j] = u
    
    return graph, u_index
                

def minCut(graph):
    
    while len(graph)>2:
        u, v= pickRandEdge(graph)
        removeSelfLoop(*randContraction(graph, u, v))
    cut = len(graph[0][1:])
    return cut

def repTrials(graph,trials):
    
    graph_cp = copy.deepcopy(graph)
    min = minCut(graph_cp)
    for i in range(trials):
        # if multiprocessing.current_process().name == "ForkPoolWorker-1":
        #     percentage_completed = i / trials * 100
        #     print(f'>> {trials} / {i} (% {percentage_completed:.2f})',
        #           end="", flush=True)
        graph_cp = copy.deepcopy(graph)
        result = minCut(graph_cp)
        if min > result:
            min = result
    return min


def mp_minCut(graph):
    # doing multi threading to solve it faster. The result was 17 for the dataset.
    graph_cp = copy.deepcopy(graph)
    min = minCut(graph_cp)
    trials = int(len(graph)**2 *math.log(len(graph)))
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as p:
            p_trial_num = math.ceil(trials / multiprocessing.cpu_count())
            results = p.starmap(repTrials, [(graph, p_trial_num)
                                                for _ in range(multiprocessing.cpu_count())])
            p.close()
            p.join()
    min_cut = np.min(results)
    return min_cut

sample = [[1,2,5], [2,1,5,6,3], [3,2,7,4],[4,3,7,8],[5,1,2,6],[6,5,2,7],[7,6,3,4,8],[8,7,4]]

def main():
    with open("kargerMinCut.txt", "r", encoding='utf-8') as file:
        arr = [[int(i) for i in line.split('\t') if i != ''] for line in file.read().strip().splitlines()]
        print(mp_minCut(sample))
    
if __name__ == "__main__": 
    main()




