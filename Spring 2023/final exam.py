# class Node
#
# Instance variables:
#    Data - the value
#    Next - the next node

class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None

class LinkedList:
    def __init__(self, d=None):
        if (d == None): # an empty list
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header
    def nextCurrent(self):
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header
    def resetCurrent(self):
        self.Current = self.Header
    def getCurrent(self):
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None
    def insertBeginning(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp
    def insertCurrentNext(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp
    def removeBeginning(self):
        if (self.Header is None): # if list is empty
            return None
        else:                     # if list not empty
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans
    def removeCurrentNext(self):
        if (self.Current.Next is None): # if there is no node
            return None                 #        after Current
        else:                           # if there is
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans
    def printList(self,msg="====="):
        p = self.Header
        print("====",msg)
        while (p is not None):
            print(p.Data, end=" ")
            p = p.Next
        if (self.Current is not None):
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")
        input("----------------")
    
    def swap(self):
        if self.Header is None or self.Current.Next is None:
            return -1
        else:
            x = self.Current.Data
            self.Current.Data = self.Current.Next.Data
            self.removeCurrentNext()
            self.insertCurrentNext(x)

            return 0


'''
class Node:
    def __init__(self, d):
        self.Data, self.Left, self.Right = d, None, None

class Tree:
    def __init__(self, d=None):
        if (d == None): # an empty tree
            self.Root = None
        else:
            self.Root = Node(d)
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d):   # if no node left insert here
                if (n.Left == None):
                    n.Left = Node(d)
                else:          # or try left child
                    __insertHere__(n.Left, d)
            elif (n.Data < d): # if no node right insert here
                if (n.Right == None):
                    n.Right = Node(d)
                else:          # or try right child
                    __insertHere__(n.Right, d)
        if (self.Root == None): # it was an empty tree
            self.Root = Node(d)
        else:
            if (self.Root.Data > d):          # try left child
                if (self.Root.Left == None):  # if empty insert here
                    self.Root.Left = Node(d)
                else:                         # try left subtree
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d):        # try right child
                if (self.Root.Right == None): # if empty insert here
                    self.Root.Right = Node(d)
                else:                         # try right subtree
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
        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")
    def printPostorder(self):
        def __visit__(n, h):
            if (n != None):
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
                print("---"*h, n.Data)
        print("==========")
        __visit__(self.Root, 1)
        print("==========")
    
    def inOrderRank(self, num):
        def create_rank_list(self):
            rank_list = []
            def __visit__(n):
                if (n != None):
                    __visit__(n.Left)
                    rank_list.append(n.Data)
                    __visit__(n.Right)
            
            __visit__(self.Root)
            return rank_list
        
        x = create_rank_list()

        for i in range(len(x)):
            if x[i] == num:
                return i
        return -1            


def compare_arrays(A, B):
    def check(arr1, arr2):
        ans = []
        for i in range(len(arr1)):
            count = 0
            for j in range(len(arr2)):
                if arr1[i] == arr2[j]:
                    count = count + 1
            if count == 0:
                ans.append(arr1[i])
            print("i = ", i, "and ans =", ans)
        return ans
    
    C1 = check(A,B)
    C2 = check(B,A)
    return C1 + C2

A = [20, 40, 70, 30, 10, 80, 50, 90, 60]
B = [35, 45, 55, 60, 50, 40]

print(compare_arrays(A,B))
'''

def find_max(A, right):
    print("Params: ", A, right)
    if right == 0:
        print("Return: ", A[right])
        return A[right]
    else:
        x = find_max(A, right - 1)
        print(A[right], " compared to ", x)
        if A[right] > x:
            print("Return: ", A[right])
            return A[right]
        else:
            print("Return: ", x)
            return x

A =  [17, 62, 49, 73, 26, 51]
find_max(A, 5)


def main():


    my_list = LinkedList()
    my_list.insertBeginning(70)
    my_list.insertBeginning(60)
    my_list.insertBeginning(50)
    my_list.insertBeginning(40)
    my_list.insertBeginning(20)
    #my_list.printList()

    my_list.resetCurrent()
    print(my_list.getCurrent())
    my_list.nextCurrent()
    my_list.nextCurrent()
    print(my_list.getCurrent())
    
    my_list.swap()
    my_list.printList()

    

#main()