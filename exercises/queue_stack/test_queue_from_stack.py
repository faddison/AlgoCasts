class Stack(object):

    def __init__(self):
        self.array = []
        self.size = 0

    def push(self, x):
        self.array.append(None)
        self.array[self.size] = x
        self.size = self.size + 1

    def pop(self):
        if self.size == 0:
            return None
        self.size = self.size - 1
        return self.array[self.size]

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.array[self.size-1]

    def length(self):
        return self.size

class Queue(object):

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size = 0

    def add(self, x):
        self.s1.push(x)

    def remove(self):
        while (self.s1.peek() is not None):
            self.s2.push(self.s1.pop())
        item = self.s2.pop()
        while (self.s2.peek() is not None):
            self.s1.push(self.s2.pop())
        return item

    def peek(self):
        while (self.s1.peek() is not None):
            self.s2.push(self.s1.pop())
        item = self.s2.peek()
        while (self.s2.peek() is not None):
            self.s1.push(self.s2.pop())
        return item

    def length(self):
        pass
        

# def test_length():
#     q = Queue()
#     assert q.length() == 0

# def test_can_add():
#     q = Queue()
#     q.add(3)
#     q.add(2)
#     assert q.length() == 2

def test_peek0():
    q = Queue()
    assert q.peek() is None

def test_peek1():
    q = Queue()
    q.add(1)
    assert q.peek() == 1

def test_peek2():
    q = Queue()
    q.add(1)
    q.add(2)
    assert q.peek() == 1

def test_peek3():
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.remove()
    assert q.peek() == 2
    
def test_remove_single():
    q = Queue()
    q.add(3)
    assert q.remove() == 3

def test_remove_double():
    q = Queue()
    q.add(3)
    q.add(2)
    assert q.remove() == 3
    
def test_order1():
    q = Queue()
    q.add(1)
    assert q.remove() == 1 
    
def test_order2():
    q = Queue()
    q.add(1)
    q.add(2)
    assert q.remove() == 1
    assert q.remove() == 2

def test_order3():
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3