import sys
import threading

def read_file(filePath: str):

    file = open(filePath, 'r')
    num_nodes = 875714
    Lines = file.readlines()

    G = [[] for i in range(num_nodes)]
    G_rev = [[] for i in range(num_nodes)]

    for Line in Lines:
        nodes = Line.split()
        # 1 to n -> 0 to n-1
        G[int(nodes[0])-1] += [int(nodes[1])-1]
        G_rev[int(nodes[1])-1] += [int(nodes[0])-1]
        
    return G, G_rev


# 1. DFS Loop 1 on G rev

def dfs_util_1(graph, v):
    global t, visited
    
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs_util_1(graph, i)
            
    finish[t] = v
    t = t+1
        
def dfs_1(graph, num_nodes):
    global t, visited, finish
    
    visited = [False]*num_nodes
    finish = [None]*num_nodes
    t = 0
    
    for i in reversed(range(num_nodes)):
        if visited[i] == False:
            dfs_util_1(i, visited)
    return finish

# 2. DFS Loop 2 on Finishing Time

def dfs_util_2(graph, i):
    global visited, scc_size
    
    visited[i] = True
    for j in graph[i]:
        if visited[j] == False:
            dfs_util_2(graph, j)

def dfs_2(graph, num_nodes):
    global visited, scc_size, finish
    
    visited = [False]*num_nodes
    scc = []
    
    for i in reversed(range(num_nodes)):
        if visited[finish[i]] == False:
            scc_size = 0
            dfs_util_1(graph, finish[i])
            scc.append(scc_size)
            
    return scc

def main():
    num_nodes = 875714
    G, G_rev = read_file("Chapter2\\2-1 SCC.txt")
    finish = dfs_1(G_rev, num_nodes)
    scc = dfs_2(G, num_nodes)
    print(','.join(map(lambda x: str(x), sorted(scc)[::-1][:5])))

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target