import heapq

def read_file(filepath):
    file = open(filepath, 'r')
    
    sym_number = int(file.readline())

    weights = file.readlines()
    sym_weight = []
    weight_sum = 0
    for weight in enumerate(weights):
        a = weight[0]
        b = int((weight[1].split('\n'))[0])
        sym_weight.append([a, b])
        
    sym_weight = sorted(sym_weight, key=lambda x: x[1])
    
    return sym_weight


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
  
        # symbol name (character)
        self.symbol = symbol
  
        # node left of current node
        self.left = left
  
        # node right of current node
        self.right = right
  
        # tree direction (0/1)
        self.huff = ''
  
    def __lt__(self, nxt):
        return self.freq < nxt.freq


def printNodes(node, val=''):
  
    # huffman code for current node
    newVal = val + str(node.huff)
  
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
  
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


sym_weight = read_file('Chapter3\\3-3 Huffman.txt')

nodes = []
for i, x in enumerate(sym_weight):
    heapq.heappush(nodes, node(x[1], x[0]))

while len(nodes) > 1:
  
    # Sort All the Nodes in Ascending Order
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
  
    # Assign Directional Value to these Nodes
    left.huff = 0
    right.huff = 1
  
    # Combine the 2 Smallest Nodes to Create New Node
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
  
    heapq.heappush(nodes, newNode)

print(nodes[0].symbol)
