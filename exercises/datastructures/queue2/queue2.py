class Queue2(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:len(self.items)]
        return item

    def size(self):
        return len(self.items)

    # 4:00 all