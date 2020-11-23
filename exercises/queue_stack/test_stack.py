import pytest

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

# def test_length():
#     s = Stack()
#     assert s.length() == 0

# def test_can_push():
#     s = Stack()
#     s.push(3)
#     s.push(2)
#     assert s.length() == 2

# def test_peek0():
#     s = Stack()
#     assert s.peek() is None

# def test_peek1():
#     s = Stack()
#     s.push(1)
#     assert s.peek() == 1

# def test_peek2():
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     assert s.peek() == 2

# def test_peek3():
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.pop()
#     assert s.peek() == 2
    
# def test_remove_single():
#     s = Stack()
#     s.push(3)
#     assert s.pop() == 3

# def test_remove_double():
#     s = Stack()
#     s.push(3)
#     s.push(2)
#     assert s.pop() == 2
    
# def test_order1():
#     s = Stack()
#     s.push(1)
#     assert s.pop() == 1 
    
# def test_order2():
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     assert s.pop() == 2
#     assert s.pop() == 1

# def test_order3():
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     assert s.pop() == 3
#     assert s.pop() == 2
#     assert s.pop() == 1