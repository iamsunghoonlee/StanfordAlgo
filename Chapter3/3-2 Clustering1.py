def read_file(filepath: str):
    file = open(filepath, 'r')
    
    a = file.readline()
    num_nodes = int(a)

    Lines = file.readlines()
    edges = [[] for i in range(num_nodes)]
    for Line in Lines:
        a = Line.split(' ')
        edges[int(a[0])-1].append([int(a[1])-1, int(a[2])])
        edges[int(a[1])-1].append([int(a[0])-1, int(a[2])])
    return num_nodes, edges

class Graph:
    def __init__(self, num_nodes):
        self.v = num_nodes
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    # Union + Find
    def find(self, parent, v):
        if parent[v] != v:
            parent[v] = self.find(parent, parent[v])
        return parent[v]
        
    def union(self, parent, rank, u, v):
        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[v] = u
            rank[u] += 1

    def clustering(self, target: int):

        self.edges = sorted(self.edges, key=lambda x: x[2])
        parent = []
        rank = []
        result = []

        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        # Variable to track the status of operation
        # i : to move through the edges
        # j : to track number of included edges
        i = 0
        j = 0
        max_edge = 0

        # Stop at target where you count 'Max Spacing'
        while j <= self.v - target:
            u, v, w = self.edges[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # Include edge only when not causing cycle
            if x != y:
                j += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                max_spacing = w

        return max_spacing

def main():
    num_nodes, edges = read_file('Chapter3//3-2 Clustering1.txt')
    graph = Graph(num_nodes)
    for a in enumerate(edges):
        for b in a[1]:
            graph.add_edge(a[0], b[0], b[1])
    max_spacing = graph.clustering(4)
    return print(max_spacing)

if __name__ == '__main__':
    main()