class Dequeue(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def pushFront(self, item):
        self.items.insert(0, item)

    def pushBack(self, item):
        self.items.append(item)

    def popFront(self):
        item = self.items[0]
        self.items = self.items[1:self.size()]
        return item

    def popBack(self):
        if len(self.items) > 0:
            item = self.items[self.size()-1]
            self.items = self.items[0:self.size()-1] # maybe 2 here
            return item
        else:
            return None
        
    def peekBack(self):
        if len(self.items) > 0:
            return self.items[self.size()-1]
        else:
            return None

    def peekFront(self):
        return self.items[0]

    def pretty(self):
        print(self.items)