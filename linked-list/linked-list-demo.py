class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Node({self.data}, {self.next_node})'


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_items = 0

    # This is O(1) complexity since our new node is the HEAD node
    def insert_start(self, data):
        self.num_items += 1
        new_node = Node(data)
        # The node being inserted is the first node in the linked list
        if self.head is None:
            self.head = new_node
        # The node being inserted is not the first node in the linked list
        else:
            # Update current head to point to the current node's next node
            new_node.next_node = self.head
            self.head = new_node

    # This is O(N) linear complexity since we have to traverse the linked list to find
    # the last node
    def insert_end(self, data):
        self.num_items += 1
        new_node = Node(data)
        # The linked list is empty and node being inserted is the first node
        if self.head is None:
            self.head = new_node
        # The linked list is not empty hence, we have to traverse to the end to add the new node
        else:
            actual_node = self.head
            # this is why the method has O(N) complexity
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node

    # This method has O(N) complexity where N is the size of the list and each node has to be
    # traversed to check if it can be removed
    def remove(self, data):
        if self.head is not None:
            actual_node = self.head
            previous_node = None
            # O(N) linear complexity
            while actual_node is not None and actual_node.data != data:
                previous_node = actual_node
                actual_node = actual_node.next_node
            # if node to be deleted is the head node
            if previous_node is None:
                self.head = actual_node.next_node
                self.num_items -= 1
            # matching node not found because we traversed to the end of the list
            elif actual_node is None:
                return
            # matching node found
            else:
                # Data is found and previous node now points to the actual node's next node
                # We don't physically remove the node, so we update the references and Garbage
                # collector will remove the unused Node object
                previous_node.next_node = actual_node.next_node
                self.num_items -= 1

    # This is O(1) complexity as we don't need to traverse the list
    def get_list_count(self):
        return self.num_items

    # This function has O(N) linear complexity
    def traverse(self):
        if self.head is not None:
            actual_node = self.head
            while actual_node is not None:
                print(actual_node)
                actual_node = actual_node.next_node
        else:
            print(f'Linked list is empty')

    def print_head(self):
        if self.head is not None:
            print(self.head)
        else:
            print(f'Linked list is empty')

    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


if __name__ == '__main__':
    print(f'Inserting items at the start')
    linked_list = LinkedList()
    linked_list.insert_start(10)
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    linked_list.insert_start('Pat')
    linked_list.insert_start(22.89)
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    print('='*50)
    print(f'Inserting items at the end')
    linked_list.insert_end(1500)
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    linked_list.insert_end('End of list')
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    print('=' * 50)
    print(f'Removing arbitrary items from the list')
    linked_list.remove('Pat')
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    linked_list.remove(22.89)
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    linked_list.remove('End of list')
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    linked_list.remove(100)
    print(f'Number of items in Linked List: {linked_list.get_list_count()}')
    linked_list.traverse()
    print('=' * 50)
    print(f'Reversing linked list without additional memory')
    linked_list.insert_start(14)
    linked_list.insert_start(53)
    linked_list.insert_start(77)
    linked_list.insert_start(29)
    linked_list.traverse()
    print(f'Linked list reversed')
    linked_list.reverse()
    linked_list.traverse()

