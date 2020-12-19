from queuestack import QueueStack

def test_length():
    q = QueueStack()
    assert q.size() == 0

def test_can_add():
    q = QueueStack()
    q.enqueue(3)
    q.enqueue(2)
    assert q.size() == 2
    
def test_remove_single():
    q = QueueStack()
    q.enqueue(3)
    assert q.dequeue() == 3

def test_remove_double():
    q = QueueStack()
    q.enqueue(3)
    q.enqueue(2)
    assert q.dequeue() == 3
    
def test_order1():
    q = QueueStack()
    q.enqueue(1)
    assert q.dequeue() == 1 
    
def test_order2():
    q = QueueStack()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_order3():
    q = QueueStack()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3