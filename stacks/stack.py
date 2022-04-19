class Stack:
    """
    Implementing Stack data structure using arrays. Stacks are LIFO (Last In First Out. Stack is
    actually an Abstract data type which is implemented using Array/Linked List data structure.

    """

    def __init__(self):
        self.elements = []

    def push(self, data: str):
        """
        Add element to the end/top of the stack. This is O(1) complexity as we are inserting
        elements at the end of the array
        :param data: str
        """
        self.elements.append(data)

    def pop(self):
        """
        Return element from top of the stack and remove it from the stack. This is O(1)
        complexity as we are removing elements from end of the array
        :return data: str
        """
        element = None
        if not self.is_empty():
            element = self.elements[-1]
            del self.elements[-1]
        return element

    def peek(self) -> str:
        """
        Return element from top of the stack. This is O(1) complexity as we are accessing element
        from the end of the array
        :return data: str
        """
        element = None
        if not self.is_empty():
            element = self.elements[-1]
        return element

    def size(self) -> int:
        """
        This function returns the length of the stack
        :return len: int
        """
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

    def print_elements(self):
        if not self.is_empty():
            print(f'Stack size: {self.size()}')
            print("\n".join([str(e) for e in self.elements]))
        else:
            print(f'Stack is empty')


if __name__ == '__main__':
    s = Stack()
    print('=' * 40)
    print('Pushing elements to stack')
    s.push("Pep")
    s.push("Jose")
    s.print_elements()
    print('=' * 40)
    print('Pushing more elements to stack')
    s.push("Mikel")
    s.push("Steven")
    s.push("Jurgen")
    s.push("Carlo")
    s.push("Simeone")
    s.print_elements()
    print('=' * 40)
    print('Pop and Peek elements of stack')
    print(f'Last element is: {s.peek()}')
    print(f'{s.pop()} popped from stack')
    print(f'Last element is: {s.peek()}')
    print(f'{s.pop()} popped from stack')
    print('=' * 40)
    s.print_elements()

