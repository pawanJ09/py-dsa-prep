class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Node(data:{self.data}, next_node:{self.next_node}, previous_node:{self.previous_node})'


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    # Unlike singly linked list this is not O(N) complexity since in doubly linked list we
    # already have the reference of the tail. Hence, insertion at the end is O(1) complexity.
    def insert(self, data):
        new_node = Node(data)
        self.num_items += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def remove(self, data):
        if self.head is not None:
            actual_node = self.head
            previous_node = None
            while actual_node is not None and actual_node.data != data:
                previous_node = actual_node
                actual_node = actual_node.next_node
            if previous_node is None:
                # Item being deleted is the head node
                self.num_items -= 1
                actual_node.next_node.previous_node = None
                self.head = actual_node.next_node
            elif actual_node is None:
                # No match found
                return
            elif actual_node.next_node is None:
                # Item being deleted is the tail node
                self.num_items -= 1
                actual_node.previous_node.next_node = None
                self.tail = actual_node.previous_node
            else:
                # Deleting arbitrary item
                self.num_items -= 1
                actual_node.previous_node.next_node = actual_node.next_node
                actual_node.next_node.previous_node = actual_node.previous_node

    # Traversal is O(N) complexity for doubly linked list.
    def traverse_forward(self):
        if self.head is not None:
            actual_node = self.head
            while actual_node is not None:
                print(actual_node.__repr__())
                actual_node = actual_node.next_node

    def traverse_reverse(self):
        if self.tail is not None:
            actual_node = self.tail
            while actual_node is not None:
                print(actual_node.__repr__())
                actual_node = actual_node.previous_node

    def get_items_count(self):
        return self.num_items

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail


if __name__ == '__main__':
    dlist = DoublyLinkedList()
    dlist.insert(26)
    dlist.insert(12)
    dlist.insert(43)
    dlist.insert(77)
    print(f'Printing doubly linked list from Head. Total items: {dlist.get_items_count()}. Head '
          f'is: {dlist.get_head()}. Tail is {dlist.get_tail()}')
    dlist.traverse_forward()
    print('=' * 100)
    print(f'Adding an element to doubly linked list')
    dlist.insert(700)
    print(f'Printing doubly linked list from Tail. Total items: {dlist.get_items_count()}. Head '
          f'is: {dlist.get_head()}. Tail is {dlist.get_tail()}')
    dlist.traverse_reverse()
    print('=' * 100)
    print(f'Removing an element from doubly linked list')
    dlist.remove(12)
    print(f'Printing doubly linked list from Head. Total items: {dlist.get_items_count()}. Head '
          f'is: {dlist.get_head()}. Tail is {dlist.get_tail()}')
    dlist.traverse_forward()
    print('=' * 100)
    print(f'Removing tail element from doubly linked list')
    dlist.remove(700)
    print(f'Printing doubly linked list from Head. Total items: {dlist.get_items_count()}. Head '
          f'is: {dlist.get_head()}. Tail is {dlist.get_tail()}')
    dlist.traverse_forward()
    print('=' * 100)
    print(f'Removing head element from doubly linked list')
    dlist.remove(26)
    print(f'Printing doubly linked list from Head. Total items: {dlist.get_items_count()}. Head '
          f'is: {dlist.get_head()}. Tail is {dlist.get_tail()}')
    dlist.traverse_forward()
