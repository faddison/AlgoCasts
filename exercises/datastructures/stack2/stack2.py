class Stack2(object):

    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items[len(self.items)-1]
        self.items = self.items[0:len(self.items)-1]
        return item

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items)-1]

            # 8:00 all

        