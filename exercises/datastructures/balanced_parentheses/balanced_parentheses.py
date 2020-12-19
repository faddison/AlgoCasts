from dequeue import Dequeue

#  (), square brackets: [], and curly brackets: {}

def b(s):
    if s == '[' or s == ']':
        return 's'
    elif s == '(' or s == ')':
        return 'p'
    elif s == '{' or s == '}':
        return 'c'
    else:
        return None

def balanced_parentheses(s):
    deq = Dequeue()
    for c in s:
        deq.pushBack(c)
    if b(deq.peekFront()) != b(deq.peekBack()):
        return False
    while deq.size() > 0:
        front = deq.popFront()
        while b(front) != b(deq.peekBack()) and deq.peekBack() != None:        
            back = deq.popBack()
        back = deq.popBack()
    return deq.size() == 0 and b(front) == b(back)
