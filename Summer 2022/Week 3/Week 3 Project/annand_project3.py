
class Node:
    def __init__(self, d):
        self.Data = d
        self.Left = None
        self.Right = None

class Tree:
    def __init__(self, d=None):
        if (d== None):
            self.Root = None
        else:
            self.Root = Node(d)
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d):
                n.Left = Node(d)
            else:
                __insertHere__(n.Left, d)
        if (self.Root == None):
            self.Root = Node(d)
        else:
            if (self.Root.Data > d):
                if (self.Root.Left == None):
                    self.Root.Left = Node(d)
                else:
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d):
                if (self.Root.Right == None):
                    self.Root.Right = Node(d)
                else:
                    __insertHere__(self.Root.Right, d)
    def check(self, d):
        def __check__(n, d):
            if (n == None):
                return False
            elif (n.Data == d):
                return True
            elif (n.Data > d):
                return __check__(n.Left, d)
            elif (n.Data < d):
                return __check__(n.Right, d)
        return __check__(self.Root, d)
    def printInorder(self):
        def __visit__(n):
            if (n != None):
                __visit__(n.Left)
                print(n.Data, end=" ")
                __visit__(n.Right)
        print("\n--------")
        __visit__(self.Root)
        print("\n--------")
    def printPreorder(self):
        def __visit__(n, h):
            if (n != None):
                print("---"*h, n.Data)
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
        print("^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^")
    def printPostorder(self):
        def __visit__(n, h):
            if (n != None):
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
                print("---"*h, n.Data)
        print("========")
        __visit__(self.Root, 1)
        print("========")

def main():
    myTree = Tree
    myFileData = open("tree_data.txt", "r")
    
    for line in myFileData:
        myTree.insert(eval(line))

    
    

