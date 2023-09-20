from itertools import combinations
from collections import defaultdict

def read_file(filepath: str):
    file = open(filepath, 'r')
    
    info = file.readline()
    Lines = file.readlines()
    nodes = defaultdict(list)
    for i, Line in enumerate(Lines):
        num = int(''.join(Line.split()), 2)
        nodes[num].append(i)
    return nodes

def hamming_1(num):
    masks = [1 << i for i in range(num.bit_length())]
    code = [num ^ mask for mask in masks]
    return code

def hamming_2(num):
    masks = [(1 << i) ^ (1 << j) for (i, j) in combinations(range(num.bit_length()), 2)]
    code = [num ^ mask for mask in masks]
    return code

class UnionFind():
    def __init__(self, nodes):
        self.root = dict(zip(nodes, nodes))
        self.subtree = dict(zip(nodes, [[node]for node in nodes]))
        
    def find(self, node):
        return self.root[node]
    
    def union(self, i, j):
        pi, pj = self.root[i], self.root[j]
        if pi != pj:
            if len(self.subtree[pj]) > len(self.subtree[pi]):
                pi, pj = pj, pi
            
            for node in self.subtree[pj]:
                self.root[node] = pi
            self.subtree[pi] += self.subtree[pj]
            del self.subtree[pj]
        else:
            return
        
def kclustering(nodes):
    clusters = UnionFind(nodes)
    for num in nodes:
        for code in hamming_1(num):
            if code in nodes:
                clusters.union(num, code)

        for code in hamming_2(num):
            if code in nodes:
                clusters.union(num, code)
                
    return len(clusters.subtree.keys())

def main():
    graph = read_file('Chapter3\\3-2 Clustering2.txt')
    print(kclustering(graph))
    
if __name__ == '__main__':
    main()