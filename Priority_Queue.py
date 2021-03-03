class QUEUE:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.start_pointer = 0
        self.end_pointer = -1
        self.items = []
        for i in range(max_size):
            self.items.insert(0, 0)

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size


    def priority_enqueue(self, item):
        if self.isFull():
            print("error")
        else:
            self.size += 1
            self.end_pointer += 1
            self.end_pointer = self.end_pointer % self.max_size
            # instead of adding to the end point add based on priotity and shift items back one

    def dequeue(self):
        item = self.items[self.start_pointer]
        self.size -= 1
        self.start_pointer += 1
        self.end_pointer = self.end_pointer % self.max_size
        return item

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



q = QUEUE(5)
q.priority_enqueue(3)
q.priority_enqueue(2)
q.priority_enqueue(3)
q.priority_enqueue(1)
q.priority_enqueue(5)
q.show_list()
print("")
q.dequeue()
q.show_list()
print("")
