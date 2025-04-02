
from bst import BinarySearchTree
from avl import AVLTree
from rbt import RedBlackTree

def test_bst():
    bst = BinarySearchTree()
    for key in [20, 10, 30, 5, 15, 25, 35]:
        bst.insert(key)
    assert bst.inorder() == [5, 10, 15, 20, 25, 30, 35]
    assert bst.search(15) is not None
    assert bst.search(100) is None
    bst.delete(20)
    assert bst.inorder() == [5, 10, 15, 25, 30, 35]
    print("BST tests passed.")

def test_avl():
    avl = AVLTree()
    for key in [20, 10, 30, 5, 15, 25, 35]:
        avl.insert(key)
    assert avl.inorder() == [5, 10, 15, 20, 25, 30, 35]
    assert avl.search(15) is not None
    assert avl.search(100) is None
    avl.delete(20)
    assert avl.inorder() == [5, 10, 15, 25, 30, 35]
    print("AVL tests passed.")

def test_rbt():
    rbt = RedBlackTree()
    for key in [20, 10, 30, 5, 15, 25, 35]:
        rbt.insert(key)
    assert rbt.inorder() == [5, 10, 15, 20, 25, 30, 35]
    assert rbt.search(15) is not None
    assert rbt.search(100) is None
    rbt.delete(20)
    assert rbt.inorder() == [5, 10, 15, 25, 30, 35]
    print("RBT tests passed.")

if __name__ == "__main__":
    test_bst()
    test_avl()
    test_rbt()
