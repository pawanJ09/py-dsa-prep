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

