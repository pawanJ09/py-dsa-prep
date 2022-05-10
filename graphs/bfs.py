class Node:

    def __init__(self, name):
        self.name = name
        self.adjacent_list = []
        self.visited = False


def breadth_first_search(start_node):

    queue = [start_node]

    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacent_list:
            if not n.visited:
                n.visited = True
                queue.append(n)


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node1.adjacent_list.append(node2)
    node1.adjacent_list.append(node3)
    node2.adjacent_list.append(node4)
    node3.adjacent_list.append(node6)
    node4.adjacent_list.append(node5)
    node4.adjacent_list.append(node7)
    breadth_first_search(node1)







