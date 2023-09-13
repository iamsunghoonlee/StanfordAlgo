from queue import PriorityQueue

def read_file(filePath: str):
    file = open(filePath, 'r')
    
    A = [line.split('\n') for line in file]
    A_L = []
    for a in A:
        a_l = []
        A_L.append(a[0].split('\t'))

    # Nested List
    edge_list = []    
    for a_l in A_L:
        i_edge_list = []
        for i in range(1, len(a_l)-1):
            i_edge = []
            s_a_l = a_l[i].split(',')
            
            i_edge.append(int(s_a_l[0])-1)
            i_edge.append(int(s_a_l[1]))
            
            i_edge_list.append(i_edge)
        edge_list.append(i_edge_list)
        
    return edge_list



def dijkstra_sp(edge_list, start: int, num_nodes: int):
    global visited, sp_value, sp_edges
    
    visited = [False]*num_nodes # To Check Every Node Not Visited
    sp_value = [2**10]*num_nodes # To Check SP to Every Node (Start with Infinite)
    to_be_visited = [] # To Check Node to be Visited
    
    # # Starting Condition
    # pq = PriorityQueue()
    # pq.put((0, start))
    visited[start] = True
    sp_value[start] = 0
    to_be_visited.append(start)
    
    while len(to_be_visited) != 0:
        next = to_be_visited.pop(0)
        visited[next] = True
        
        for dest in edge_list[next]:
            to_be_visited.append(dest[0])
            if sp_value[next] + dest[1] <= sp_value[dest[0]]:
                sp_value[dest[0]] = sp_value[next] + dest[1]
                
    return sp_value
   
            
def main():
    edge_list = read_file('Chapter2\\2-2 DijkstraShortestPath.txt')
    num_nodes = 200
    start_node = 0
    sp = dijkstra_sp(edge_list, 0, 200)
    # Shortest Path toward (7,37,59,82,99,115,133,165,188,197)th vertex
    print(sp[6], sp[36], sp[58], sp[81], sp[98], sp[114], sp[132], sp[164], sp[187], sp[196])
    
if __name__ == '__main__':
    main()