class DATA_STRUCT:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.start_pointer = 0
        self.end_pointer = -1
        self.items = []
        for i in range(max_size):
            self.items.insert(0, " ")

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if self.isFull():
            print("error")
        else:
            self.size += 1
            self.end_pointer += 1
            self.end_pointer = self.end_pointer % self.max_size
            self.items[self.end_pointer] = item

    def dequeue(self):
        pass

    def size(self):
        return len(self.items)

    def print_list(self):
        print(self.items)
        print(len(self.items))

    def show_list(self):
        if self.end_pointer < self.start_pointer:
            self.end_pointer += self.max_size
        for i in range(self.start_pointer, self.end_pointer + 1):
            print(self.items[i % self.max_size])


class QUEUE(DATA_STRUCT):
    def __init__(self, max_size, name):
        self.name = name
        super().__init__(max_size)

    def dequeue(self):
        item = self.items[self.start_pointer]
        self.size -= 1
        self.start_pointer += 1
        self.end_pointer = self.end_pointer % self.max_size
        return item


class STACK(DATA_STRUCT):
    def __init__(self, max_size, name):
        self.name = name
        super().__init__(max_size)

    def dequeue(self):
        item = self.items[self.end_pointer]
        self.size -= 1
        self.end_pointer -= 1
        self.end_pointer = self.end_pointer % self.max_size
        return item


q = QUEUE(5, "queue")
print(q.name)
q.enqueue("one")
q.enqueue("two")
q.enqueue("three")
q.enqueue("four")
q.enqueue("five")
q.show_list()
print("")
q.dequeue()
q.show_list()
print("")

s = STACK(5, "stack")
print(s.name)
s.enqueue("one")
s.enqueue("two")
s.enqueue("three")
s.enqueue("four")
s.enqueue("five")
s.show_list()
print("")
s.dequeue()
s.show_list()
print("")