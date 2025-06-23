import random

class TreeNode:
    def __init__(self, alerta):
        self.alerta = alerta
        self.left = None
        self.right = None

class AlertBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, alerta):
        if not self.root:
            self.root = TreeNode(alerta)
        else:
            self._insert(self.root, alerta)

    def _insert(self, node, alerta):
        # Insert by priority: lower priority to left, higher or equal to right
        if alerta.priority < node.alerta.priority:
            if node.left:
                self._insert(node.left, alerta)
            else:
                node.left = TreeNode(alerta)
        else:
            if node.right:
                self._insert(node.right, alerta)
            else:
                node.right = TreeNode(alerta)

    def get_any_alert(self):
        # For demo: get root alert (or leftmost if you want FIFO)
        return self.root.alerta if self.root else None

    def remove_root(self):
        # Remove root node (simple case, not a full BST delete)
        if not self.root:
            return None
        alerta = self.root.alerta
        if self.root.right:
            self.root = self.root.right
        elif self.root.left:
            self.root = self.root.left
        else:
            self.root = None
        return alerta

    def is_empty(self):
        return self.root is None

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.alerta)
                _inorder(node.right)
        _inorder(self.root)
        return result