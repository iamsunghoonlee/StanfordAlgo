def read_file(filepath):
    with open(filepath, 'r') as f:
        ver_num = int(f.readline())
        ver_weights = []
        for line in f.readlines():
            ver_weights.append(int(line))
    return ver_num, ver_weights

def mwis(vertices_num, vertices_weights):
    mwis_val = {}
    mwis_val[0] = vertices_weights[0]
    mwis_val[1] = vertices_weights[1]
    
    i = 2
    while i < vertices_num:
        mwis_val[i] = max(mwis_val[i-1], mwis_val[i-2] + vertices_weights[i])
        i += 1
    return mwis_val

def mwis_items(vertices_num, vertices_weights, mwis_val):
    ver_items = []
    
    i = vertices_num - 1
    while i >= 0:
        if mwis_val[i-1] >= mwis_val[i-2] + vertices_weights[i]:
            i -= 1
        else:
            ver_items.append(i)
            i -= 2
            
    return ver_items

def main():
    ver_num, weights = read_file('Chapter3\\3-3 MWIS.txt')
    result = mwis(ver_num, weights)
    items = mwis_items(ver_num, result, weights)
    
    # Check if index 0, 1, 2, 3, 16, 116, 516, 996 is in the mwis_items
    check_items = [0, 1, 2, 3, 16, 116, 516, 996]
    solution = []
    for i in check_items:
        if i in items:
            solution.append('1')
        else:
            solution.append('0')

    print(''.join(solution))
    
if __name__ == '__main__':
    main()