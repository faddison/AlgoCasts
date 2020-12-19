from stack2 import Stack2

def test_length():
    s = Stack2()
    assert s.size() == 0

def test_can_push():
    s = Stack2()
    s.push(3)
    s.push(2)
    assert s.size() == 2

def test_peek0():
    s = Stack2()
    assert s.peek() is None

def test_peek1():
    s = Stack2()
    s.push(1)
    assert s.peek() == 1

def test_peek2():
    s = Stack2()
    s.push(1)
    s.push(2)
    assert s.peek() == 2

def test_peek3():
    s = Stack2()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    assert s.peek() == 2
    
def test_remove_single():
    s = Stack2()
    s.push(3)
    assert s.pop() == 3

def test_remove_double():
    s = Stack2()
    s.push(3)
    s.push(2)
    assert s.pop() == 2
    
def test_order1():
    s = Stack2()
    s.push(1)
    assert s.pop() == 1 
    
def test_order2():
    s = Stack2()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_order3():
    s = Stack2()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1