from tqdm import tqdm
import numpy as np

def read_file(name):
    """Given the path/name of the file, return the empty 3-d array(n, n, n+1)"""
    file = open(name,'r')
    data = file.readlines()
    
    n = int(data[0].split()[0])
    m = int(data[0].split()[1])
    
    Array = np.zeros((n,n,n+1))
    inf = 9999

    for i in range(n):
        for j in range(n):
            if i==j:
                Array[i,j,0] = 0
            else:
                Array[i,j,0] = inf
    for index, line in enumerate(data[1:]):
        item = line.split()
        Array[int(item[0]) -1 ,int(item[1])-1,0] = int(item[2])
        
    return Array

def floyd_warshall(Array):
    """Given the empth 3-d array, return the minimum path(a numbber or 'Negative cycle').
    """
    n = Array.shape[0]
    
    for k in tqdm(range(1, n+1)):
        for i in range(n):
            for j in range(n):
                Array[i,j,k] = min(Array[i,j,k-1], Array[i,k-1,k-1]+Array[k-1,j,k-1])
                
    
    for i in range(n):
        if Array[i,i,n] <0:
            min_path = 'Negative cycle'
            return min_path
    min_path = np.min(Array[:,:,n])
    
    return min_path
    

def main():
    Array = read_file("Chapter4\\4-1 AllPairShortestPath1.txt")
    min_path = floyd_warshall(Array)
    print(min_path)

if __name__ == '__main__':
    main()