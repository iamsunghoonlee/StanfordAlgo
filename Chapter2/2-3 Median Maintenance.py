import heapq

def read_file(filePath: str):
    file = open(filePath, 'r')
    Lines = file.readlines()

    num_list = []
    for Line in Lines:
        num_list.append(int(Line))

    return num_list

heap_small = []
heap_large = []

def add_numbers(num):
    
    heapq.heappush(heap_small, -1 * num)
    
    if heap_small and heap_large and (-1*heap_small[0]) > heap_large[0] :
        val = -1*heapq.heappop(heap_small)
        heapq.heappush(heap_large, val)

    if len(heap_small) > len(heap_large) + 1:
        val = -1*heapq.heappop(heap_small)
        heapq.heappush(heap_large, val)
        
    if len(heap_large) > len(heap_small) + 1:
        val = -1*heapq.heappop(heap_large)
        heapq.heappush(heap_small, val)

def findMedian():
    global heap_small, heap_large
    
    if len(heap_small) >= len(heap_large):
        return -1*heap_small[0]
    if len(heap_small) < len(heap_large):
        return heap_large[0]

def main():
    num_list = read_file("Chapter2\\2-3 Median Maintenance.txt")
    meds = []
    
    for i in num_list:
        add_numbers(i)
        med = findMedian()
        meds.append(med)
    
    print(sum(meds) % 10000)
    
if __name__ == '__main__':
    main()
