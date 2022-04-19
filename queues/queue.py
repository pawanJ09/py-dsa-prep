class Queue:
    """
    Implementing Queue data structure using arrays. Queues are FIFO (First In First Out). Queue is
    actually an Abstract data type which is implemented using Array/Linked List data structure.
    Preferred data structure would be Doubly Linked list. Read dequeue() function for more details.

    """

    def __init__(self):
        self.elements = []

    def size(self) -> int:
        """
        This function returns the length of the queue and has O(1) complexity.
        :return: int
        """
        return len(self.elements)

    def is_empty(self) -> bool:
        """
        This function checks whether queue is empty and returns boolean. It has O(1) complexity.
        :return: bool
        """
        return self.elements == []

    def enqueue(self, data: int):
        """
        This function inserts elements to the end of the queue. This has O(1) complexity as we
        don't have to perform linear search to get to the last item
        :param data: int
        """
        self.elements.append(data)

    def dequeue(self):
        """
        This function removes the first element from the queue. This has O(N) complexity since
        after removing first element array has to be adjusted for all subsequent elements. Better
        solution would be to use Doubly Linked list as we would have access to the head and tail
        elements however, the space complexity would increase
        :return element: int
        """
        element = -1
        if not self.is_empty():
            element = self.elements[0]
            del self.elements[0]
        return element

    def peek(self):
        """
        This function returns the first element from the queue. This has O(1) complexity as we
        are only returning the first element and not deleting anything.
        :return:
        """
        if not self.is_empty():
            return self.elements[0]
        return -1

    def print_elements(self):
        if not self.is_empty():
            print(f'Queue size: {self.size()}')
            print("\n".join([str(e) for e in self.elements]))
        else:
            print(f'Queue is empty')


if __name__ == "__main__":
    q = Queue()
    print('=' * 40)
    print('Adding elements to queue')
    q.enqueue(27)
    q.enqueue(11)
    q.print_elements()
    print('=' * 40)
    print('Adding more elements to queue')
    q.enqueue(7)
    q.enqueue(89)
    q.enqueue(17)
    q.enqueue(101)
    q.enqueue(122)
    q.print_elements()
    print('=' * 40)
    print('Dequeue and Peek elements of queue')
    print(f'First element is: {q.peek()}')
    print(f'{q.dequeue()} removed from queue')
    print(f'First element is: {q.peek()}')
    print(f'{q.dequeue()} removed from queue')
    print('=' * 40)
    q.print_elements()
