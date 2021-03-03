class Binary_Tree_Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


    def insertNode(self, insertval):
        if self.value:
            if insertval < self.value:
                if self.left is None:
                    self.left = Binary_Tree_Node(insertval)
                else:
                    self.left.insertNode(insertval)
            elif insertval > self.value:
                if self.right is None:
                    self.right = Binary_Tree_Node(insertval)
                else:
                    self.right.insertNode(insertval)
        else:
            self.value = insertval

    def search_tree(self, searchval):
        if self.value is not None:
            print(self.value)
            if searchval == self.value:
                print("The value" + searchval + "has been found")
                return
            elif searchval < self.value:
                self.left.search_tree(searchval)
            else:
                self.right.search_tree(searchval)

root = Binary_Tree_Node(15)
root.insertNode(13)
root.insertNode(10)
root.insertNode(17)
root.insertNode(20)
root.search_tree(20)
