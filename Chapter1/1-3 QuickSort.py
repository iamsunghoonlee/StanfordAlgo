# 1. Read the File and Clean up the Data

def read_file(filepath : str):
    f = open(filepath, "r")
    lines = f.readlines()
    integer_list = [int((i.split('\n'))[0]) for i in lines]
    return integer_list


# 2. Choose Pivot Fuction

def choose_pivot_1(A: list):
    pivot = 0
    return pivot

def choose_pivot_2(A: list):
    pivot = len(A) - 1
    return pivot

def choose_pivot_3(A: list):    
    p1 = 0
    if len(A)//2 == len(A)/2:
        p2 = len(A)//2 - 1
    else:
        p2 = len(A)//2
    p3 = len(A)-1

    # Getting Median among Three Candidates
    if ((A[p1] < A[p2] and A[p2] < A[p3]) or (A[p3] < A[p2] and A[p2] < A[p1])) :
        pivot = p2
    elif ((A[p2] < A[p1] and A[p1] < A[p3]) or (A[p3] < A[p1] and A[p1] < A[p2])) :
        pivot = p1
    else :
        pivot = p3
    return pivot



# 3. Partition Functions

def partition(A: list, pivot: int):
    A[0], A[pivot] = A[pivot], A[0]
    p = A[0]
    
    i, j = 1, 1
    for j  in range(1, len(A)):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[0], A[i-1] = A[i-1], A[0]
    
    return A, i


# 4. Quick Sort Function

def quick_sort_1(A: list):
    comp = len(A)-1
    pivot = choose_pivot_1(A)
    
    if len(A) <= 1:
        return (A, 0)
    else:
        A, i = partition(A, pivot)
        A[:i-1], comp_l = quick_sort_1(A[:i-1])
        A[i:], comp_r = quick_sort_1(A[i:])
    return (A, comp + comp_l + comp_r)


def quick_sort_2(A: list):
    comp = len(A)-1
    pivot = choose_pivot_2(A)
    
    if len(A) <= 1:
        return (A, 0)
    else:
        A, i = partition(A, pivot)
        A[:i-1], comp_l = quick_sort_2(A[:i-1])
        A[i:], comp_r = quick_sort_2(A[i:])
    return (A, comp + comp_l + comp_r)


def quick_sort_3(A: list):
    comp = len(A)-1
    pivot = choose_pivot_3(A)
    
    if len(A) <= 1:
        return (A, 0)
    else:
        A, i = partition(A, pivot)
        A[:i-1], comp_l = quick_sort_3(A[:i-1])
        A[i:], comp_r = quick_sort_3(A[i:])
    return (A, comp + comp_l + comp_r)
        

def main():
    A = read_file("Chapter1\\1-3 QuickSort.txt")
    
    # Problem 1
    A1 = A.copy()
    qs1 = quick_sort_1(A1)
    print(qs1[1])
    
    # Problem 2
    A2 = A.copy()
    qs2 = quick_sort_2(A2)
    print(qs2[1])
    
    # Problem 3 
    A3 = A.copy()
    qs3 = quick_sort_2(A3)
    print(qs3[1])

if __name__ == '__main__':
    main()