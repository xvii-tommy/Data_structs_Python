class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class linkedlist:
    def __init__(self):
        self.headval = None

    def printlinkedlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def addstart(self, data):
        newnode = Node(data)
        newnode.nextval = l_list.headval
        l_list.headval = newnode

    def addend(self, data):
        newnode = Node(data)
        if self.headval == None:
            self.headval = data
            return
        lastnode = self.headval
        while lastnode.nextval:
            lastnode = lastnode.nextval
        lastnode.nextval = newnode

    def insertnode(self, priornode, data):
        if priornode == None:
            print("node not in list")
            return
        newnode = Node(data)
        newnode.nextval = priornode.nextval
        priornode.nextval = newnode

    def removenode(self, node):
        pass


l_list = linkedlist()
l_list.headval = Node("jan")
n2 = Node("feb")
n3 = Node("mar")

l_list.headval.nextval = n2
n2.nextval = n3

l_list.addstart("dec")
l_list.addend("apr")
l_list.insertnode(n2, "jul")

l_list.printlinkedlist()


