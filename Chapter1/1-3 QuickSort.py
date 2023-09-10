# 1. Read the File and Clean up the Data

def read_file(filepath : str):
    f = open(filepath, "r")
    lines = f.readlines()
    integer_list = [int((i.split('\n'))[0]) for i in lines]
    return integer_list


# 2. Choose Pivot Fuction

# 2-1. First Element of the input array
def choose_pivot_1(A: list):
    pivot = 0
    return pivot
# 2-2. Last Element of the input array
def choose_pivot_2(A: list):
    pivot = len(A)-1
    return pivot

# 2-3. Median Element of the input array
def choose_pivot_3(A: list):
    # Median Candidates
    p1 = 0
    p3 = len(A)-1
    if len(A)//2 == len(A)/2:
        p2 = len(A)//2 - 1
    else:
        p2 = len(A)//2
    
    # Getting Median among Three Candidates
    if ((A[p1] < A[p2] and A[p2] < A[p3]) or (A[p3] < A[p2] and A[p2] < A[p1])) :
        pivot = p2
    elif ((A[p2] < A[p1] and A[p1] < A[p3]) or (A[p3] < A[p1] and A[p1] < A[p2])) :
        pivot = p1
    else :
        pivot = p3
    return pivot


# 3. Partition Functions

def partition(A: list, l: int, r: int, pivot: int):
    # Swapping Chosen Pivot and the First Item
    A[0], A[pivot] = A[pivot], A[0]
    
    p = A[0]
    i = l+1
    for j  in range(l+1, r+1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]




# 4. Quick Sort Function
def quick_sort(A: list, n: int):
    if n == 1:
        return A
    
    else:


# def main():
#     A = read_file("Chapter1\\1-3 QuickSort.txt")
    
#     # Problem 1
    
#     # Problem 2
    
#     # Problem 3 


# if __name__ == '__main__':
#     main()