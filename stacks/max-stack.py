class MaxStack:

    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data: int):
        self.main_stack.append(data)
        if self.is_max_stack_empty():
            self.max_stack.append(data)
        elif data > self.max_stack[-1]:
            self.max_stack.append(data)

    def get_max(self):
        if not self.is_max_stack_empty():
            element = self.max_stack[-1]
            del self.max_stack[-1]
            return element
        return -1

    def is_main_stack_empty(self):
        return self.main_stack == []

    def is_max_stack_empty(self):
        return self.max_stack == []

    def print_elements(self):
        if not self.is_main_stack_empty():
            print('=' * 50)
            print('\n'.join([str(e) for e in self.main_stack]))
        else:
            print('Main stack is empty')

    def main_stack_size(self):
        return len(self.main_stack)

    def max_stack_size(self):
        return len(self.max_stack)


if __name__ == '__main__':
    ms = MaxStack()
    ms.push(89)
    ms.push(45)
    ms.push(12)
    ms.push(167)
    ms.push(189)
    ms.push(77)
    print('=' * 50)
    print(f'Main stack size: {ms.main_stack_size()}')
    ms.print_elements()
    print('=' * 50)
    print(f'Max stack size: {ms.max_stack_size()}')
    print('=' * 50)
    print(f'Max element from stack is {ms.get_max()}')