import heapq

if __name__ == '__main__':
    heap = [1, 5, 99, 18, 78, 22, 11, 100]
    # Updates the provided array/list as a min heap using heapify function
    heapq.heapify(heap)
    print(f'Min Heap {heap}')
    for i in range(len(heap)):
        print(f'Popping {heapq.heappop(heap)}')
    heap = [1, 5, 99, 18, 78, 22, 11, 100]
    nums = []
    # Creating new array/list as min heap using heappush function
    for value in heap:
        heapq.heappush(nums, value)
    for i in range(len(nums)):
        print(f'Popping {heapq.heappop(nums)}')

