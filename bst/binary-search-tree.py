class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data: int):
        # First insert as BST is empty
        if not self.root:
            node = Node(data)
            self.root = node
        # BST is not empty
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data: int, node):
        # Going to the left since data is less than parent data
        if data < node.data:
            # There are more nodes on the left hence looping again
            if node.left:
                self.insert_node(data, node.left)
            # No more left nodes hence adding data to the left
            else:
                node.left = Node(data, node)
        # Going to the right since data is more than parent data
        else:
            # There are more nodes on the right hence looping again
            if node.right:
                self.insert_node(data, node.right)
            # No more right nodes hence adding data to the right
            else:
                node.right = Node(data, node)

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)
        return -1

    def get_min_value(self, node):
        if node.left:
            return self.get_min_value(node.left)
        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)
        return -1

    def get_max_value(self, node):
        if node.right:
            return self.get_max_value(node.right)
        return node.data

    def traverse(self):
        if self.root:
            self.traverse_inorder(self.root)
        return -1

    def traverse_inorder(self, node):
        if node.left:
            self.traverse_inorder(node.left)
        print(node.data)
        if node.right:
            self.traverse_inorder(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(25)
    bst.insert(13)
    bst.insert(2)
    bst.insert(89)
    bst.insert(55)
    bst.insert(10)
    bst.insert(100)
    bst.insert(97)
    print(f'Max Value {bst.get_max()}')
    print(f'Min Value {bst.get_min()}')
    bst.traverse()
