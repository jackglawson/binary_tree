class BinaryTree:
    """
    Binary tree of size n with members 1 to n.
    indexes[i] stores the (left, right) daughters of member i.
    -1 indicates the absence of a daughter.
    """
    def __init__(self, indexes):
        self.indexes = indexes
        self.inorder = []

    def inorder_traversal(self):
        self.inorder = []
        self._inorder(1)
        return self.inorder

    def _inorder(self, root):
        if root == -1:
            return
        subtrees = self.indexes[root - 1]
        self._inorder(subtrees[0])
        self.inorder.append(root)
        self._inorder(subtrees[1])


binary_tree = BinaryTree([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]])
print(binary_tree.inorder_traversal())
