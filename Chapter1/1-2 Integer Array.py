# 1. Read the File and Clean up the Data
def read_file(filepath : str):
    f = open(filepath, "r")
    lines = f.readlines()
    integer_list = [int((i.split('\n'))[0]) for i in lines]
    return integer_list


# 2. Merging Lists and Counting Split Inversion Function (Used inside Sort and Count Function)
def merge_and_count_split_inv(L1: list, L2: list):
    # L1, L2 : sorted list / n = list length
    # List to store sorted integers
    L = [0]*(len(L1) + len(L2))

    # i to track L1, j to track L2, k to track L
    i = 0
    j = 0
    k = 0
    count = 0

    while i <= len(L1) - 1 and j <= len(L2) - 1:
        if L1[i] < L2[j]:
            L[k] = L1[i]
            i += 1
            k += 1

        elif L1[i] > L2[j]:
            L[k] = L2[j]
            count += len(L1) - i
            j += 1
            k += 1

    while i <= len(L1) - 1:
        L[k] = L1[i]
        i += 1
        k += 1

    while j <= len(L2) - 1:
        L[k] = L2[j]
        j += 1
        k += 1

    return L, count


# 3. Sort and Count Function
def sort_and_count(A: list):
    if len(A) == 1:
        return A, 0
      
    else:
        mid = len(A)//2
        
        B, x = sort_and_count(A[:mid])
        C, y  = sort_and_count(A[mid:])
        D, z = merge_and_count_split_inv(B, C)

    return D, x+y+z



def main():
    A = read_file("Chapter1\\1-2 Integer Array.txt")
    print(sort_and_count(A)[1])


if __name__ == '__main__':
    main()
