#   Directions
#  1) Create a node class.  The constructor
#  should accept an argument that gets assigned
#  to the data property and initialize an
#  empty array for storing children. The node
#  class should have methods 'add' and 'remove'.
#  2) Create a tree class. The tree constructor
#  should initialize a 'root' property to null.
#  3) Implement 'traverseBF' and 'traverseDF'
#  on the tree class.  Each method should accept a
#  function that gets called with each element in the tree

class Node(object):

    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))
        # print("add:len={0}".format(len(self.children)))

    def remove(self, data):
        # print("remove:len={0}".format(len(self.children)))
        for i in range(0,len(self.children)):
            if self.children[i] is not None and self.children[i].data == data:
                self.children[i] = None

class Tree(object):

    def __init__(self):
        self.root = None

    def traverseBF(self, func):
        nodes = []
        nodes.append(self.root)
        while len(nodes) > 0:
            # print("len={0}".format(len(nodes)))
            n = nodes[0]
            func(n)
            nodes = nodes[1:len(nodes)]
            nodes.extend(n.children)

    def traverseDF(self, func):
        nodes = []
        nodes.append(self.root)
        while len(nodes) > 0:
            # print("len={0}".format(len(nodes)))
            n = nodes[0]
            func(n)
            nodes = nodes[1:len(nodes)]
            # print("pre-nodes-len:{0}".format(len(nodes)))
            children = n.children
            children.reverse()
            for c in children:
                nodes.insert(0, c)
            