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
        while (True):
            if data < curr.data:
                if curr.left: 
                    curr = curr.left
                else:
                    curr.left = Node(data)
                    return
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(data)
                    return
    
    def contains(self, target):
        curr = self.root
        if curr.data == target: return True
        while (True):
            if curr.data == target: return True
            if target < curr.data:
                if curr.left: curr = curr.left
                else: return False
            else:
                if curr.right: curr = curr.right
                else: return False

    # def validate(self):
    #     validateHelp

    # def validateHelper(self, curr, lessthan):
    #     if not curr: return 0
    #     if curr.left < curr:
    #         return validateHelper()+validateHelper()