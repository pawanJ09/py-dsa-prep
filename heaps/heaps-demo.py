CAPACITY = 10


class Heap:
    """
    We don't use Heap data structure to insert or remove arbitrary items because that would
    result in linear search to first find the item and then perform the operation resulting in O(
    N) complexity. For such cases Binary Search Trees or AVL Trees would be used since they
    result in O(logN) time complexity. Heaps are used in cases where we need to find the min or
    max element with O(1) time complexity but the heapify takes O(logN) time complexity.
    """

    def __init__(self):
        """
        Initialize the min_heap. Since this is a min_heap the topmost element will be the node
        that has the smallest value.
        """
        self.heap_size = 0
        self.min_heap = [0]*CAPACITY

    def insert(self, data):
        """
        Data is always inserted at the end of the heap and then heapify is invoked to reorder and
        have the min node as the root/parent node. This operation is O(1) but the heapify is O(logN)
        hence this operation has O(logN) complexity
        :param data: int
        """
        # If heap is at capacity then return
        if (self.heap_size+1) == CAPACITY:
            return -1
        # Add the data at the end of the heap and fix the root/parent node with heapify logic
        curr_heap_size = self.heap_size
        self.min_heap[curr_heap_size] = data
        self.heap_size += 1
        self.fix_up(curr_heap_size)

    def fix_up(self, index):
        """
        Function to reorder the heap so the root/parent node is the node with the smallest value.
        If this had been a max heap then exactly the reverse. Here we are going from child to
        root/parent hence going up
        """
        # Right child
        if (index % 2) == 0:
            parent = (index-2)//2
        else:
            parent = (index-1)//2
        if index > 0 and self.min_heap[parent] > self.min_heap[index]:
            # Root/Parent node will now become node with lower value since this is min heap
            self.min_heap[parent], self.min_heap[index] = self.min_heap[index], self.min_heap[
                parent]
            self.fix_up(parent)

    def fix_down(self, index):
        # Calculate left and right child from the root/parent node
        left_index = (2 * index) + 1
        right_index = (2 * index) + 2
        min_index = index
        # Here we are doing < so to skip the last element which is now the popped min/max element
        if left_index < self.heap_size and self.min_heap[min_index] > self.min_heap[left_index]:
            min_index = left_index
        if right_index < self.heap_size and self.min_heap[min_index] > self.min_heap[right_index]:
            min_index = right_index
        # Swap with min index to reorder the heap
        if index != min_index:
            self.min_heap[index], self.min_heap[min_index] = self.min_heap[min_index], \
                                                             self.min_heap[index]
            self.fix_down(min_index)

    def get_min(self):
        """
        This is similar to peek function for queue and this returns the minimum value from the heap
        :return:
        """
        return self.min_heap[0]

    def poll(self):
        """
        This function will return the minimum item and remove it from the heap. It will then
        heapify the existing elements in the heap
        :return data: int
        """
        min_element = self.min_heap[0]
        # Swap root node with the last item in the heap and decrement the heap size
        self.min_heap[0], self.min_heap[self.heap_size-1] = \
            self.min_heap[self.heap_size-1], self.min_heap[0]
        self.heap_size -= 1
        self.fix_down(0)
        return min_element

    def heap_sort(self):
        for _ in range(self.heap_size):
            min_element = self.poll()
            print(min_element)


if __name__ == '__main__':
    heap = Heap()
    heap.insert(23)
    heap.insert(9)
    heap.insert(78)
    heap.insert(56)
    heap.insert(18)
    heap.insert(100)
    heap.heap_sort()


