class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            node = Node(data)
            self.root = node
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # Insertion is similar to a binary tree
        # If data is less than node's value then we go with left tree
        if data < node.data:
            # If left node exists then invoke recursively
            if node.left:
                self.insert_node(data, node.left)
            # Left node doesn't exist, so we add on the left
            else:
                node.left = Node(data)
                node.height = max(self.cal_height(node.left), self.cal_height(node.right)) + 1
        else:
            # If right node exists then invoke recursively
            if node.right:
                self.insert_node(data, node.right)
            # Right node doesn't exist, so we add on the left
            else:
                node.right = Node(data)
                node.height = max(self.cal_height(node.left), self.cal_height(node.right)) + 1

    def cal_height(self, node):
        # This is the case for NULL node
        if node is None:
            return -1
        return node.height

    def cal_balance(self, node):
        # Balance for NULL nodes is 0
        # Balance of an AVLTree = left_height = right_height
        # If positive then it is a left heavy subtree and if negative then it is a right
        # heavy subtree. The tree is balanced if the balance is 0.
        if node is None:
            return 0
        return self.cal_height(node.left) - self.cal_height(node.right)

    def violation_helper(self, node):
        balance = self.cal_balance(node)
        # Left heavy tree
        if balance > 1:
            # left-right heavy situation. Left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left) < 0:
                self.rotate_left(node.left)
            self.rotate_right(node.right)
        if balance < -1:
            # right-left heavy situation. Right rotation on parent + left rotation on grandparent
            if self.calculate_balance(node.right) < 0:
                self.rotate_right(node.right)
            self.rotate_left(node.left)

    def handle_violations(self, node):
        while node is not None:
            node.height = max(self.cal_height(node.left), self.cal_height(node.right)) + 1
            self.violation_helper(node)
            node = node.parent

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
                if parent is not None and parent.left == node:
                    node.left = None
                elif parent is not None and parent.right == node:
                    parent.right = None
                elif parent is None:
                    self.root = None
                del node
                # Here we are invoking this method because AVL tree is balanced as compared to
                # traditional BST.
                self.handle_violations(parent)
            # 2.a. Right child exists
            elif node.left is None and node.right is not None:
                print(f'Removing node with right child: {node.data}')
                parent = node.parent
                if parent is not None and parent.left == node:
                    parent.left = node.right
                if parent is not None and parent.right == node:
                    parent.right = node.right
                if parent is None:
                    self.root = node.right
                del node
                # Here we are invoking this method because AVL tree is balanced as compared to
                # traditional BST.
                self.handle_violations(parent)
            # 2.b. Right child exists
            elif node.left is not None and node.right is None:
                print(f'Removing node with left child: {node.data}')
                parent = node.parent
                if parent is not None and parent.left == node:
                    parent.left = node.left
                if parent is not None and parent.right == node:
                    parent.right = node.left
                if parent is None:
                    self.root = node.left
                del node
                # Here we are invoking this method because AVL tree is balanced as compared to
                # traditional BST.
                self.handle_violations(parent)
            # #. Both children exist
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


