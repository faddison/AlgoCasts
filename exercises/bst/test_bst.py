from bst import BST, Node

def test_insert1():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(17)
    assert bst.root.data == 10
    assert bst.root.left.data == 5
    assert bst.root.right.data == 15
    assert bst.root.right.right.data == 17

def test_insert2():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(0)
    bst.insert(-5)
    bst.insert(3)
    assert bst.root.left.left.right.data == 3

def test_contains1():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(0)
    bst.insert(-5)
    bst.insert(3)
    assert bst.contains(10) == True

def test_contains2():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(0)
    bst.insert(-5)
    bst.insert(3)
    assert bst.contains(1) == False

def test_contains3():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(0)
    bst.insert(-5)
    bst.insert(3)
    assert bst.contains(3) == True

def test_contains4():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(0)
    bst.insert(-5)
    bst.insert(3)
    assert bst.contains(0) == True

def test_contains5():
    root = Node(10)
    bst = BST(root)
    assert bst.contains(10) == True
