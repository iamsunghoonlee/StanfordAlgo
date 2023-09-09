# 1. Read the File and Clean up the Data
def read_file(filepath : str):
    f = open(filepath, "r")
    lines = f.readlines()
    integer_list = [int((i.split('\n'))[0]) for i in lines]
    return integer_list


# 2. Counting Inversion Function
def merge_and_count_split_inv(L1: list, L2: list, n: int):
    # L1, L2 : sorted list / n = list length
    # List to store sorted integers
    L = [0]*n

    # i to track L1, j to track L2, k to track L
    i = 0
    j = 0
    k = 0

    while i <= len(L1) - 1 and j <= len(L2) - 1:
        if L1[i] < L2[j]:
            L[k] = L1[i]
            i += 1
            k += 1

        elif L1[i] > L2[j]:
            L[k] = L2[j]
            j += 1
            k += 1

    while i <= len(L1) - 1:
        L[k] = L1[i]
        i += 1
        k += 1

    while j <= len(L2) - 1:
        L[k] = L1[j]
        j += 1
        k += 1

    return L



def sort_and_count(A: list, n: int):
    if n == 1:
        return 0
      
    else:
        B, x = sort_and_count(A[(n//2):], (n/2))
        C, y = sort_and_count(A[:(n//2)], (n/2))
        split = merge_and_count_split_inv(B, C, n)
    return 

# def main()
#     read_file()
#     count_inversion()

    
# if __name__ == '__main__':
#     main()
