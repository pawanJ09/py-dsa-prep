class QueueStack:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def is_enqueue_empty(self):
        return self.enqueue_stack == []

    def is_dequeue_empty(self):
        return self.dequeue_stack == []

    def push(self, data: int):
        self.enqueue_stack.append(data)

    def pop(self):
        if not self.is_enqueue_empty():
            if self.is_dequeue_empty():
                while not self.is_enqueue_empty():
                    self.dequeue_stack.append(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()
        if not self.is_dequeue_empty():
            return self.dequeue_stack.pop()
        return -1

    def print_elements(self):
        if not self.is_enqueue_empty():
            print('=' * 50)
            print('Enqueue stack')
            print('\n'.join(str(e) for e in self.enqueue_stack))
        elif not self.is_dequeue_empty():
            print('=' * 50)
            print('Dequeue stack')
            print('\n'.join(str(e) for e in self.dequeue_stack))
        else:
            print(f'Enqueue stack is empty')


if __name__ == '__main__':
    qs = QueueStack()
    qs.push(89)
    qs.push(12)
    qs.push(1002)
    qs.push(67)
    qs.push(99)
    qs.print_elements()
    print(f'Popped element in Queue style from Stack: {qs.pop()}')
    print(f'Popped element in Queue style from Stack: {qs.pop()}')
    print(f'Popped element in Queue style from Stack: {qs.pop()}')