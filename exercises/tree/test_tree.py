from tree import Node, Tree

def test_tree_node_data():
    n = Node(1)
    assert n.data == 1

def test_tree_node_add_child():
    n = Node(1)
    n.add(2)
    assert n.children[0].data == 2

def test_tree_node_add_childAndSibling():
    n = Node(1)
    n.add(2)
    n.add(3)
    assert n.children[0].data == 2
    assert n.children[1].data == 3
    
def test_tree_node_add_grandchild():
    n = Node(1)
    n.add(2)
    n.children[0].add(3)
    assert n.children[0].children[0].data == 3

def test_tree_node_remove_data_match():
    n = Node(1)
    n.add(2)
    n.remove(2)
    assert n.children[0] == None

def test_tree_node_remove_data_mismatch():
    n = Node(1)
    n.add(2)
    n.remove(3)
    assert n.children[0] != None
    
def test_tree_node_remove_data_parentmatch():
    n = Node(1)
    n.remove(1)
    try:
        n.children[0]
    except Exception as e:
        assert str(e) == 'list index out of range'

def test_tree_node_remove_data_multi_same_match():
    n = Node(1)
    n.add(2)
    n.add(3)
    n.remove(2)
    n.remove(2)
    assert n.children[0] == None
    assert n.children[1].data == 3

def test_tree_node_remove_data_multi_diff_match():
    n = Node(1)
    n.add(2)
    n.add(3)
    n.remove(2)
    n.remove(3)
    assert n.children[0] == None
    assert n.children[1] == None

def test_tree_traverseBF_root():
    n = Node(0)
    t = Tree()
    t.root = n
    f = lambda n : print("data={0}".format(n.data))
    t.traverseBF(f)

def test_tree_traverseBF_1child():
    n = Node(0)
    n.add(20)
    t = Tree()
    t.root = n
    f = lambda n : print("data={0}".format(n.data))
    t.traverseBF(f)

def test_tree_traverseBF_1sibling():
    n = Node(0)
    n.add(20)
    n.add(21)
    t = Tree()
    t.root = n
    f = lambda n : print("data={0}".format(n.data))
    t.traverseBF(f)

def test_tree_traverseBF_1direct_grandchild():
    n = Node(0)
    n.add(20)
    n.add(21)
    n.children[0].add(30)
    t = Tree()
    t.root = n
    f = lambda n : print("data={0}".format(n.data))
    t.traverseBF(f)

def test_tree_traverseBF_1direct_grandchild1sibling():
    n = Node(0)
    n.add(20)
    n.add(21)
    n.children[0].add(30)
    n.children[0].add(31)
    t = Tree()
    t.root = n
    f = lambda n : print("data={0}".format(n.data))
    t.traverseBF(f)

def test_tree_traverseBF_1indirect_grandchild():
    n = Node(0)
    n.add(20)
    n.add(21)
    n.children[1].add(30)
    t = Tree()
    t.root = n
    f = lambda n : print("data={0}".format(n.data))
    t.traverseBF(f)

def test_tree_traverseBF_1both_grandchild1sibling():
    n = Node(0)
    n.add(20)
    n.add(21)
    n.children[0].add(30)
    n.children[1].add(31)
    t = Tree()
    t.root = n
    f = lambda n : print("data={0}".format(n.data))
    t.traverseBF(f)