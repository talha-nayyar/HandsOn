
from bst import BinarySearchTree

class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'

class RedBlackTree(BinarySearchTree):
    def insert(self, key):
        new_node = RBNode(key)
        self.root = self._bst_insert(self.root, new_node)
        self._fix_insert(new_node)

    def _bst_insert(self, root, node):
        if not root:
            return node
        if node.key < root.key:
            root.left = self._bst_insert(root.left, node)
            root.left.parent = root
        else:
            root.right = self._bst_insert(root.right, node)
            root.right.parent = root
        return root

    def _fix_insert(self, k):
        while k != self.root and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u and u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u and u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
        self.root.color = 'black'

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
