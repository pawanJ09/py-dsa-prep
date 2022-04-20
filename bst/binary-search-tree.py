class TreeComparator:
    def compare(self, node1, node2):
        # in case node1 or node2 are none
        if not node1 or not node2:
            return node1 == node2
        # check the values
        if node1.data != node2.data:
            return False
        # run recursively for left and right nodes
        return self.compare(node1.left, node2.left) and self.compare(node1.right, node2.right)


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

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)
        else:
            # 3 scenarios
            # 1. Leaf node case
            if node.left is None and node.right is None:
                print(f'Removing leaf node: {node.data}')
                parent = node.parent
                # Remove reference of left child
                if parent is not None and parent.left == node:
                    parent.left = None
                # Remove reference of right child
                if parent is not None and parent.right == node:
                    parent.right = None
                # Node doesn't have a parent and hence is a root node
                if parent is None:
                    self.root = None
                del node
            # 2.a. Left child exists for node being deleted
            elif node.left is None and node.right is not None:
                print(f'Removing node with right child: {node.data}')
                parent = node.parent
                if parent is not None and parent.left == node:
                    parent.left = node.right
                if parent is not None and parent.right == node:
                    parent.right = node.right
                if parent is None:
                    self.root = node.right
                node.right.parent = parent
                del node
            # 2.b. Right child exists for node being deleted
            elif node.left is not None and node.right is None:
                print(f'Removing node with left child: {node.data}')
                parent = node.parent
                if parent is not None and parent.left == node:
                    parent.left = node.left
                if parent is not None and parent.right == node:
                    parent.right = node.left
                if parent is None:
                    self.root = node.left
                node.left.parent = parent
                del node
            # 3. Node being removed has both children
            else:
                print(f'Removing items with both children: {node.data}')
                # Predecessor is the largest leaf node on the left side.
                # Swap the values with the predecessor and remove the predecessor node since its
                # easier to remove the leaf node as per scenario 1
                predecessor = self.get_predecessor(node.left)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

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
    bst.insert(-5)
    print(f'Max Value {bst.get_max()}')
    print(f'Min Value {bst.get_min()}')
    bst.traverse()
    print('=' * 50)
    print(f'Removing nodes')
    bst.remove(200)
    bst.remove(13)
    bst.remove(2)
    bst.traverse()
    print('=' * 50)
    print(f'Comparing 2 binary search trees')
    bst1 = BinarySearchTree()
    bst1.insert(25)
    bst1.insert(89)
    bst1.insert(55)
    bst1.insert(10)
    bst1.insert(100)
    bst1.insert(97)
    bst1.insert(-5)
    bst2 = BinarySearchTree()
    bst2.insert(25)
    bst2.insert(89)
    bst2.insert(55)
    bst2.insert(10)
    bst2.insert(100)
    bst2.insert(97)
    bst2.insert(-5)
    comp = TreeComparator()
    print(f'2 trees identical? {comp.compare(bst1.root, bst2.root)}')
