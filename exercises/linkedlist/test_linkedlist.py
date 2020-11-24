class Node(object):

    def __init__(self, data, node):
        self.data = data
        self.next = node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insertFirst(self, data):
        if self.head is not None:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data, None)
        self.size = self.size + 1

    def size(self):
        return self.size

    def getFirst(self):
        return self.head

    def getLast(self):
        n = self.head
        while (n.next is not None):
            n = n.next
        return n

    def clear(self):
        self.head = None
        self.size = 0

    def removeFirst(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None
            self.size = self.size - 1

    def removeLast(self):
        if self.head is not None:
            if self.head.next is not None:
                n1 = self.head
                n2 = self.head.next
                while n2.next is not None:
                    n1 = n2
                    n2 = n2.next
                n1.next = None
            else:
                self.head = None
            self.size = self.size - 1

    def insertLast(self, data):
        if self.head is not None:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data, None)
        else:
            self.head = Node(data, None)
        self.size = self.size + 1

    def getAt(self, index):
        n = self.head
        count = 0
        if index == 0:
            return n
        else:
            while n.next is not None:
                count = count + 1
                if count == index:
                    return n.next
                else:
                    n = n.next
            return None

    def removeAt(self, index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                self.size = self.size - 1
        else:
            while n.next is not None:
                count = count + 1
                if count == index:
                    return n.next
                else:
                    n = n.next
            return None

    def insertAt(self, data, node):
        pass

    def forEach(self, func):
        pass

def test_node_data():
    n = Node('test', None)
    assert n.data == 'test'

def test_node_next():
    n = Node(None, None)
    assert n.next == None

def test_linked_new():
    l = LinkedList()
    assert l.head == None

def test_linked_size0():
    l = LinkedList()
    assert l.size == 0
    
def test_linked_insertFirst_size():
    l = LinkedList()
    l.insertFirst('test')
    assert l.size == 1

def test_linked_insertFirst_size3():
    l = LinkedList()
    l.insertFirst('test')
    l.insertFirst('test')
    l.insertFirst('test')
    assert l.size == 3

def test_linked_insertFirst_head():
    l = LinkedList()
    l.insertFirst('test')
    assert l.head.data == 'test'
    
def test_linked_insertFirst_order():
    l = LinkedList()
    l.insertFirst('1')
    l.insertFirst('2')
    l.insertFirst('3')
    assert l.head.data == '3'

def test_linked_insertFirst_order_chain():
    l = LinkedList()
    l.insertFirst('1')
    l.insertFirst('2')
    l.insertFirst('3')
    assert l.head.data == '3'
    assert l.head.next.data == '2'
    assert l.head.next.next.data == '1'

def test_linked_getFirst():
    l = LinkedList()
    l.insertFirst(1)
    n = l.getFirst()
    assert n.data == 1

def test_linked_getFirst_3():
    l = LinkedList()
    l.insertFirst(1)
    l.insertFirst(2)
    l.insertFirst(3)
    n = l.getFirst()
    assert n.data == 3
    
def test_linked_getLast():
    l = LinkedList()
    l.insertFirst(1)
    n = l.getLast()
    assert n.data == 1

def test_linked_getLast_3():
    l = LinkedList()
    l.insertFirst(1)
    l.insertFirst(2)
    l.insertFirst(3)
    n = l.getLast()
    assert n.data == 1

def test_clear_node():
    l = LinkedList()
    l.insertFirst(1)
    l.clear()
    assert l.head == None

def test_clear_size():
    l = LinkedList()
    l.insertFirst(1)
    l.clear()
    assert l.size == 0

def test_removeFirst_null():
    l = LinkedList()
    l.removeFirst()
    assert l.head == None
    assert l.size == 0

def test_removeFirst_1():
    l = LinkedList()
    l.insertFirst(1)
    l.removeFirst()
    assert l.head == None
    assert l.size == 0

def test_removeFirst_3():
    l = LinkedList()
    l.insertFirst(1)
    l.insertFirst(2)
    l.insertFirst(3)
    l.removeFirst()
    assert l.head.data == 2
    assert l.head.next.data == 1
    assert l.size == 2

def test_removeLast_Head():
    l = LinkedList()
    l.insertFirst(1)
    l.removeLast()
    assert l.head == None
    assert l.size == 0

def test_removeLast_Next():
    l = LinkedList()
    l.insertFirst(1)
    l.insertFirst(2)
    l.removeLast()
    assert l.head.data == 2
    assert l.head.next == None
    assert l.size == 1

def test_removeLast_3():
    l = LinkedList()
    l.insertFirst(1)
    l.insertFirst(2)
    l.insertFirst(3)
    l.removeLast()
    assert l.head.data == 3
    assert l.head.next.data == 2
    assert l.head.next.next == None
    assert l.size == 2

def test_removeLast_multi():
    l = LinkedList()
    l.insertFirst(1) # 1
    l.insertFirst(2) # 2->1
    l.removeLast() # 2
    l.insertFirst(3) # 3->2
    l.insertFirst(4) # 4->3->2
    l.removeLast() # 4->3
    assert l.head.data == 4
    assert l.head.next.data == 3
    assert l.head.next.next == None
    assert l.size == 2

def test_insertLast_head():
    l = LinkedList()
    l.insertLast(1)
    assert l.size == 1
    assert l.head.data == 1

def test_insertLast_2():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    assert l.size == 2
    assert l.head.data == 1
    assert l.head.next.data == 2

def test_insertLast_3():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    assert l.size == 3
    assert l.head.data == 1
    assert l.head.next.data == 2
    assert l.head.next.next.data == 3

def test_insertLast_complex():
    l = LinkedList()
    l.insertFirst(1) # 1
    l.insertFirst(2) # 2->1
    l.insertLast(5) # 2->1->5
    l.insertLast(7) # 2->1->5->7
    l.removeLast() # 2->1->5
    l.insertFirst(3) # 3->2->1->5
    l.insertLast(6)  # 3->2->1->5->6
    l.insertFirst(4) # 4->3->2->1->5->6
    l.removeLast() # 4->3->2->1->5
    assert l.size == 5
    assert l.head.data == 4
    assert l.head.next.data == 3
    assert l.head.next.next.data == 2
    assert l.head.next.next.next.data == 1
    assert l.head.next.next.next.next.data == 5 

def test_getAt_head_None():
    l = LinkedList()
    n = l.getAt(0)
    assert n == None

def test_getAt_head():
    l = LinkedList()
    l.insertLast(1)
    n = l.getAt(0)
    assert n.data == 1

def test_getAt_2():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    n = l.getAt(1)
    assert n.data == 2

def test_getAt_2b():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    n = l.getAt(0)
    assert n.data == 1

def test_getAt_2_fail():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    n = l.getAt(2)
    assert n == None

