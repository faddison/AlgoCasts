from stack2 import Stack2

class QueueStack(object):

    def __init__(self):
        self.s1 = Stack2()
        self.s2 = Stack2()

    def size(self):
        return self.s1.size()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        while self.s1.size() > 0:
            self.s2.push(self.s1.pop())
        item = self.s2.pop()
        while self.s2.size() > 0:
            self.s1.push(self.s2.pop())
        return item