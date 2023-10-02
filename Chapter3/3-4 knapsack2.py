def read_file(filepath):
    with open(filepath, 'r') as f:
        info = f.readline().split('\n')[0].split(' ')
        allowed_size = int(info[0])
        num_item = int(info[1])
        
        value = []
        weight = []
        
        for line in f.readlines():
            temp = line.split('\n')[0]
            temp = temp.split(' ')
            value.append(int(temp[0]))
            weight.append(int(temp[1]))

    return allowed_size, num_item, value, weight      

def knapsack (allowed_size, num_item, value, weight):
    A = [[0 for x in range(allowed_size + 1)] for x in range(num_item + 1)]
    
    for i in range(num_item + 1):
        for j in range(allowed_size + 1):
            if i == 0 or j == 0:
                A[i][j] = 0
            elif weight[i-1] <= j:
                A[i][j] = max(value[i-1] + A[i-1][j - weight[i-1]], A[i-1][j])
            else:
                A[i][j] = A[i-1][j]
                
    return A[num_item][allowed_size]

def main():
    allowed_size, num_item, value, weight = read_file('Chapter3\\3-4 knapsack2.txt')
    sol = knapsack(allowed_size, num_item, value, weight)
    print(sol)
    
if __name__ == '__main__':
    main()