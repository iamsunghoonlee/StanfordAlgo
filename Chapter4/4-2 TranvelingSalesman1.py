import numpy as np
import math
from itertools import combinations
from tqdm.auto import tqdm

def read_file(filepath):
    with open(filepath, 'r') as f:
        num_vertices = int(f.readline())
        
        data = f.readlines()
        
        inf = 9999
        dist = [[0 for i in range(num_vertices + 1)] for j in range(num_vertices + 1)]
        
        for a, b in combinations(range(num_vertices), 2):
            sa = data[a].split()
            sb = data[b].split()
            distance = math.sqrt((float(sa[0]) - float(sb[0]))**2 + (float(sa[1]) - float(sb[1]))**2)
            dist[a+1][b+1] = distance

    return dist

def find_subset(arr, k):
    """Given array arr and integer k, find the combinations of subsets. With 1 prepend.
    """
    sub = []
    a = list(combinations(arr, k))
    for i in a:
        i = tuple([1]+list(i))
        sub.append(i)
    return sub


def tsp_dest(A, dist, subset, j):
    # Given subset and j, find the minimum value
    
    # Remove the destination(last vertice)
    subset = list(subset)
    subset.remove(j)
    
    s_removed = subset
    
    if len(s_removed)>1:
    
        s_removed = tuple(s_removed)
        mini = min(A[(s_removed, k)] + dist[k][j] for k in s_removed)
    
    else:
        s_removed = 1
        mini = A[(1, 1)] + dist[j][1]
    
    return mini


def tsp_ori(A, dist):
    # Given the whole matrix(graph), find the minimum value of traveling salesman problem
    mini = min(A[(tuple(range(1,len(dist))), j)] + dist[j][1] for j in range(2,len(dist)))
    
    return mini


def tsp(name):

    dist = read_file(name)
    num = len(dist) - 1
    
    # Initialize the matrix
    inf = 1e6
    A = {}
    A[(1,1)] = 0
    
    subsets = {} # key = "m" (size), value = subsets under "m" (size)
    indices = []
    for m in range(1, num):
        current_subset = []
        S = find_subset(range(2,num+1), m)
        for j in S:
            A[(j,1)] = inf
            indices.append(j)
            current_subset.append(j)
        subsets[m+1] = current_subset

    # Fill in the graph(matrix)
    for m in tqdm(range(2, num+1)):
        for subset in tqdm(subsets[m]):
            s = subset
            
            for j in s:
                if j != 1:
                    A[(s,j)] = tsp_dest(A, dist, s, j)
                   
    # Find the minimum value
    mini = tsp_ori(A, dist)
    return mini
    
def main():
    mini = tsp('Chapter4\\4-2 TravelingSalesman1.txt')
    print(mini)

if __name__ == '__main__':
    main()