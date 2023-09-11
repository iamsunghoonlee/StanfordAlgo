import random

def read_file(filepath : str):
    f = open(filepath, "r")
    lines = f.readlines()
    g = []
    
    for line in lines:
        f_l = (line.split("\n")[0])
        f_l = f_l.split("\t")
        f_l.remove('')
        # items append to list
        line = []
        for i in f_l:
            line.append(int(i)-1)
        g.append(line)

    # for i in range(len(g)):
    #     g[i].remove(i)
    
    return g

g = read_file("Chapter1\\1-4 Karger MinCut.txt")
print(g[0])

# 0. Edge Count
def edge_count(graph):
    count = 0
    for i in range(len(graph)):
        if len(graph[i]) >= 1:
            count += 1
    return count

# 1. Pick Edge Randomly
def random_choice(graph):
    u = []
    v = []
    for i in range(len(graph)):
        if len(graph[i]) >= 1:
            u.append(i)
    random_u = random.choice(u)
    
    for i in graph[random_u]:
        v.append(i)
    random_v = random.choice(v)
    return random_u, random_v

# 2. Merge u and v into a single vertex, remove loops
def merge_vertices(graph, u: int, v: int):
    if u >= v:
        # Add Edges to the Other Vertex
        for i in graph[v]:
            graph[u].append(i)
            
        # Clear Edge Info
        graph[u].remove(v)
        graph[u].remove(u)
        graph[v].clear()
        # Replace Merged Vertex
        for i in graph:
            if v in i:
                i.remove(v)
                i.append(u)
        # Remove Loop
        for i in range(len(graph)):
            loop = graph[i].count(i)
            while loop > 0:
                graph[i].remove(i)
                loop -= 1

    if u < v:
        # Add Edges to the Other Vertex
        for i in graph[u]:
            graph[v].append(i)
            
        # Clear Edge Info
        graph[v].remove(v)
        graph[v].remove(u)
        graph[u].clear()
        # Replace Merged Vertex
        for i in graph:
            if u in i:
                i.remove(u)
                i.append(v)
        # Remove Loop
        for i in range(len(graph)):
            loop = graph[i].count(i)
            while loop > 0:
                graph[i].remove(i)
                loop -= 1

    return graph

# 3. Karger MinCut : Repeat the group of functions until one edge left (2 vertices)
def karger_mincut(graph):
    while edge_count(graph) > 2:
        print(edge_count(graph))
        u, v = random_choice(graph)
        merge_vertices(graph, u, v)
    
    # Count Edges
    for i in graph:
        if len(graph[i]) > 0:
            edge_num = len(graph[i])
    return graph, edge_num



# def main():
#     g = read_file("Chapter1\\1-4 Karger MinCut.txt")
#     graph = g.copy()
#     print(karger_mincut(graph)[1])
    
# if __name__ == '__main__':
#     main()