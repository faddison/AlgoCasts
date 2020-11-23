import pytest

class Queue(object):

    def __init__(self):
        self.array = []
        self.size = 0

    def add(self, x):
        self.array.append(None) # make sure theres space
        self.array[self.size] = x
        self.size = self.size + 1

    def remove(self):
        item = self.array[0]
        for i in range(1, self.size):
            self.array[i-1] = self.array[i]
        self.size = self.size - 1
        return item

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.array[0]

    def length(self):
        return self.size

# [1,2,3], [4,5,6] => [1,4,2,5,3,6]
def weave(q1, q2):
    q3 = Queue()
    while (q1.peek() is not None or q2.peek() is not None):
        if q1.peek() is not None:
            tmp = q1.remove()
            q3.add(tmp)
        if q2.peek() is not None:
            q3.add(q2.remove())
    return q3

def test_weave_equal():
    q1 = Queue()
    q1.add(1)
    q1.add(2)
    q1.add(3)    
    q2 = Queue()
    q2.add(4)
    q2.add(5)
    q2.add(6)    
    q3 = weave(q1, q2)
    assert q3.remove() == 1
    assert q3.remove() == 4
    assert q3.remove() == 2
    assert q3.remove() == 5
    assert q3.remove() == 3
    assert q3.remove() == 6

def test_weave_unequal():
    q1 = Queue()
    q1.add(1)
    q1.add(2)   
    q2 = Queue()
    q2.add(4)
    q2.add(5)
    q2.add(6) 
    q2.add(7)   
    q3 = weave(q1, q2)
    assert q3.remove() == 1
    assert q3.remove() == 4
    assert q3.remove() == 2
    assert q3.remove() == 5
    assert q3.remove() == 6
    assert q3.remove() == 7

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