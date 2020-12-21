class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        curr = self.root
        inserted = False
        while (not inserted):
            if data < curr.data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(data)
                    inserted = True
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(data)
                    inserted = True
    
    def contains(self, target):
        pass