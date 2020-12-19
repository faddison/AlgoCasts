from queue2 import Queue2

def test_length():
    q = Queue2()
    assert q.size() == 0

def test_can_add():
    q = Queue2()
    q.enqueue(3)
    q.enqueue(2)
    assert q.size() == 2
    
def test_remove_single():
    q = Queue2()
    q.enqueue(3)
    assert q.dequeue() == 3

def test_remove_double():
    q = Queue2()
    q.enqueue(3)
    q.enqueue(2)
    assert q.dequeue() == 3
    
def test_order1():
    q = Queue2()
    q.enqueue(1)
    assert q.dequeue() == 1 
    
def test_order2():
    q = Queue2()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_order3():
    q = Queue2()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3