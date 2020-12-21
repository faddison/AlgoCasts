from bst import BST, Node

def test1():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(17)
    assert bst.root.data == 10
    assert bst.root.left.data == 5
    assert bst.root.right.data == 15
    assert bst.root.right.right.data == 17

def test2():
    root = Node(10)
    bst = BST(root)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(0)
    bst.insert(-5)
    bst.insert(3)
    assert bst.root.left.left.right.data == 3

# test('Contains returns null if value not found', () => {
#   const node = new Node(10);
#   node.insert(5);
#   node.insert(15);
#   node.insert(20);
#   node.insert(0);
#   node.insert(-5);
#   node.insert(3);

#   expect(node.contains(9999)).toEqual(null);
# });
