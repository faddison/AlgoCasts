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
    # case 1: index == 0, self.head == None [done]
    # case 2: index != 0, self.head == None [done]
    # case 3: index == 0, self.head != None && self.next == None [done]
    # case 4: index == 0, self.head != None && self.next != None [done]
    # case 5: index != 0, self.head != None && self.next == None [done]
    # case 6*: index != 0, self.head != None && self.next != None (iteration)
    # case 6: index unreachable [done]
    # case 7: index reached, next unreachable [done]
    # case 8: index reached, next reachable [done]

    # todo: to improve performance check size against index before hand
    def removeAt(self, index):
        if self.head != None:   
            if self.head.next != None:
                if index == 0: # case 4
                    self.head = self.head.next
                    self.size = self.size - 1
                    return 4
                else: # case 6*
                    count = 1
                    n0 = self.head
                    n1 = self.head.next
                    while n1.next != None and count < index:
                        n0 = n1
                        n1 = n1.next
                        count = count + 1
                    if count < index: # case 6 (index unreachable)
                        return 6
                    elif count == index and n1.next == None: # case 7: index reached, next unreachable (truncation)
                        n0.next = None
                        self.size = self.size - 1
                        return 7
                    elif count == index and n1.next != None: # case 8: index reached, next reachable (reorganization)
                        n0.next = n1.next
                        self.size = self.size - 1
                        return 8
                    else:
                        raise Exception("Case 6. Paths a, b, and c not encountered. Possible additional case found.")
            else:                 
                if index == 0: # case 3
                    self.head = None
                    self.size = self.size - 1
                    return 3              
                else: # case 5 (index out of range)
                    return 5
        else: # case 1, 2
            if index == 0:
                return 1
            else:
                return 2

    def insertAt(self, data, index):
        if index < 0:
            return 0
        if self.head == None:
            self.head = Node(data, None)
            self.size = self.size + 1
            return 1
        else: # head exists
            if index == 0:
                self.head = Node(data, self.head)
                self.size = self.size + 1
                return 2
            else: # head exists, head.next exists, index >=2
                n = self.head
                count = 0
                while n.next != None and count < index:
                    n = n.next
                    count = count + 1
                if n.next == None: # append
                    n.next = Node(data, None)
                    self.size = self.size + 1
                    return 3
                else:
                    n.next = Node(data, n.next)
                    self.size = self.size + 1
                    return 4

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

    
    
    # case 6*: index != 0, self.head != None && self.next != None (iteration)
    # case 7: index reached, next unreachable [done]
    # case 8: index reached, next reachable [done]

# case 1: index == 0, self.head == None [done]
def test_removeAt_c1_indexIsZero_headIsNone():
    l = LinkedList()
    case = l.removeAt(0)
    assert case == 1
    assert l.size == 0
    assert l.head == None

# case 2: index != 0, self.head == None [done]
def test_removeAt_c2_indexNotZero_headIsNone():
    l = LinkedList()
    case = l.removeAt(1)
    assert case == 2
    assert l.size == 0
    assert l.head == None

# case 3: index == 0, self.head != None && self.next == None [done]
def test_removeAt_c3_indexIsZero_headNotNone_headNextIsNone():
    l = LinkedList()
    l.insertFirst(1)
    case = l.removeAt(0)
    assert case == 3
    assert l.size == 0
    assert l.head == None

# case 4: index == 0, self.head != None && self.next != None [done]
def test_removeAt_c4_indexIsZero_headNotNone_headNextNotNone():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    case = l.removeAt(0)
    assert case == 4
    assert l.size == 1
    assert l.head.data == 2
    assert l.head.next == None

# case 5: index != 0, self.head != None && self.next == None [done]
def test_removeAt_c5_indexNotZero_headNotNone_headNextIsNone():
    l = LinkedList()
    l.insertFirst(1)
    case = l.removeAt(1)
    assert case == 5
    assert l.size == 1
    assert l.head.data == 1

# case 6*: index != 0, self.head != None && self.next != None (iteration)
# case 6: index unreachable [done]
def test_removeAt_c6_indexNotZero_headNotNone_headNextNotNone_indexUnreachable():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    case = l.removeAt(3)
    assert case == 6
    assert l.size == 2
    assert l.head.data == 1
    assert l.head.next.data == 2

# case 7: index reached, next unreachable [done]
def test_removeAt_c7_indexNotZero_headNotNone_headNextNotNone_indexReachable_nextUnreachable_Size2():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    case = l.removeAt(1)
    assert case == 7
    assert l.size == 1
    assert l.head.data == 1
    assert l.head.next == None

# case 7b: index reached, next unreachable (truncation)
def test_removeAt_c7b_indexNotZero_headNotNone_headNextNotNone_indexReachable_nextUnreachable_Size3():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    l.insertLast(3)
    case = l.removeAt(2)
    assert case == 7
    assert l.size == 2
    assert l.head.data == 1
    assert l.head.next.data == 2
    assert l.head.next.next == None
    
# case 8: index reached, next reachable [done]
def test_removeAt_c8_indexNotZero_headNotNone_headNextNotNone_indexReachable_nextReachable_Size3():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    l.insertLast(3)
    case = l.removeAt(1)
    assert case == 8
    assert l.size == 2
    assert l.head.data == 1
    assert l.head.next.data == 3
    assert l.head.next.next == None

def test_removeAt_c8_indexNotZero_headNotNone_headNextNotNone_indexReachable_nextReachable_Size4():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)
    case = l.removeAt(1)
    assert case == 8
    assert l.size == 3
    assert l.head.data == 1
    assert l.head.next.data == 3
    assert l.head.next.next.next == None

# --- Directions
# Return the 'middle' node of a linked list.
# If the list has an even number of elements, return
# the node at the end of the first half of the list.
# *Do not* use a counter variable, *do not* retrieve
# the size of the list, and only iterate
# through the list one time.
# --- Example
#   const l = new LinkedList();
#   l.insertLast('a')
#   l.insertLast('b')
#   l.insertLast('c')
#   midpoint(l); # returns { data: 'b' }

# cases
# 1: even
# 2: odd

def midpoint(l):
    if l.head == None:
        return None
    s = l.head
    f = l.head
    while f.next != None and f.next.next != None:
        s = s.next
        f = f.next.next
    return s

def test_midpoint_headIsNone():
    l = LinkedList()
    m = midpoint(l)
    assert m == None

def test_midpoint_headNextIsNone():
    l = LinkedList()
    l.insertFirst(1)
    m = midpoint(l)
    assert m.data == 1

def test_midpoint_headNextNext():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    m = midpoint(l)
    assert m.data == 1

def test_midpoint_even4():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)
    m = midpoint(l)
    assert m.data == 2

def test_midpoint_odd5():
    l = LinkedList()
    l.insertLast(1)
    l.insertLast(2)
    l.insertLast(3)
    l.insertLast(4)
    l.insertLast(5)
    m = midpoint(l)
    assert m.data == 3
# 0: index < 0
# 1: head == None, index == 0
# 1: head == None, index > 0
# 2: head != None, index == 0
# 3: append (end of list or index unreachable)
# 4: insertion

def test_insertAt_c0_IndexLessThanZero():
    l = LinkedList()
    case = l.insertAt(1, -1)
    assert case == 0

def test_insertAt_c1_headIsNone_IndexIsZero():
    l = LinkedList()
    case = l.insertAt(1, 0)
    assert case == 1
    assert l.head.data == 1
    assert l.size == 1

def test_insertAt_c1_headIsNone_IndexNotZero():
    l = LinkedList()
    case = l.insertAt(1, 2)
    assert case == 1
    assert l.head.data == 1
    assert l.size == 1

def test_insertAt_c2_headNotNone_IndexIsZero():
    l = LinkedList()
    l.insertFirst(1)
    case = l.insertAt(2, 0)
    assert case == 2
    assert l.head.data == 2
    assert l.head.next.data == 1
    assert l.size == 2

def test_insertAt_c3_append_IndexOutOfRange():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    case = l.insertAt(3, 10)
    assert case == 3
    assert l.head.data == 1
    assert l.head.next.data == 2
    assert l.head.next.next.data == 3
    assert l.size == 3
    
def test_insertAt_c3_append_EndOfList():
    l = LinkedList()
    l.insertFirst(1)
    l.insertLast(2)
    case = l.insertAt(3, 2)
    assert case == 3
    assert l.head.data == 1
    assert l.head.next.data == 2
    assert l.head.next.next.data == 3
    assert l.size == 3

def test_insertAt_c4_insert():
    l = LinkedList()
    l.insertFirst(1) # 0
    l.insertLast(2) # 1
    l.insertLast(3) # 2
    case = l.insertAt(4, 1)
    assert case == 4
    assert l.head.data == 1
    assert l.head.next.data == 2
    assert l.head.next.next.data == 4
    assert l.head.next.next.next.data == 3
    assert l.size == 4
