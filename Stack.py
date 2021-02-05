class STACK:
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

    def push(self, item):
        if self.isFull():
            print("error")
        else:
            self.size += 1
            self.end_pointer += 1
            self.end_pointer = self.end_pointer % self.max_size
            self.items[self.end_pointer] = item

    def pop(self):
        item = self.items[self.end_pointer]
        self.size -= 1
        self.end_pointer -= 1
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



s = STACK(5)
s.push("one")
s.push("two")
s.push("three")
s.push("four")
s.push("five")
s.show_list()
print("")
s.pop()
s.show_list()
print("")