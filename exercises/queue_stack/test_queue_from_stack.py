
class Queue(object):

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size = 0

    def add(self, x):
        pass

    def remove(self):
        pass

    def peek(self):
        pass 

    def length(self):
        pass

def test_length():
    q = Queue()
    assert q.length() == 0

def test_can_add():
    q = Queue()
    q.add(3)
    q.add(2)
    assert q.length() == 2

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