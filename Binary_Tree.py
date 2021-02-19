class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree:
    def __init__(self):
        self.root = None

    def SearchTree(self, searchval):
        printval = self.root
        while printval.value is not None:
            print(printval.value)
            if printval.value == searchval:
                return
            elif printval.value > searchval:
                printval = self.root.left

            else:
                printval = self.root.right


bt = Binary_Tree()
bt.root = Node(10)
bt.root.left = Node(5)
bt.root.right = Node(15)

bt.SearchTree(15)

