import random

def read_file(filepath: str):
    file = open(filepath, 'r')
    
    a = file.readline()
    b = a.split(' ')
    num_node = int(b[0])

    Lines = file.readlines()
    graph = [[] for i in range(num_node)]
    for Line in Lines:
        a = Line.split(' ')
        graph[int(a[0])-1].append([int(a[1])-1, int(a[2])])
        graph[int(a[1])-1].append([int(a[0])-1, int(a[2])])
                 
    return graph


def prim_mst(graph):
    # visited_vertces to compare with all_vertices, tree_edge to store visited edge
    visited_vertices = set()
    visited_vertices.add(random.choice([i for i in range(0, len(graph))]))
    cost = 0
    
    while len(visited_vertices) < len(graph):
        edge = {}
        for vertex in visited_vertices:
            for v in graph[vertex]:
                if v[0] not in visited_vertices:
                    edge[(vertex, v[0])] = v[1]
        # Find Shortest Edge
        (u,v), dist = min(edge.items(), key = lambda x : x[1])
        
        visited_vertices.add(v)
        cost += dist
        
    return cost

def main():
    graph = read_file('Chapter3\\3-1 Prim MST.txt')
    cost = prim_mst(graph)
    return print(cost)

if __name__ == '__main__':
    main()