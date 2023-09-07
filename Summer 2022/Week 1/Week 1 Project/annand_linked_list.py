#Create linked list with data from txt file 
#and allow user to insert/delete data from linked list

class Node:
    def __init__(self, d):
        '''
        Node class constructor intializes Node, the data associated with node, and the next value
        Parameters:
            self, data of Node
        Returns:
            None
        '''
        self.Data = d
        self.Next = None

class LinkedList:
    def __init__(self, d=None):
        '''
        LinkedList class constructor intializes Header as None or Node(d) and Current as None or Header
        Parameters:
            self, data of new Node
        Returns:
            None
        '''
        if (d==None):
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header
    def insertBeginning(self,d):
        '''
        insertBeginning method sets new Node as header of the linked list
        Parameters:
            self, data of new node
        Returns:
            None
        '''
        if (self.Header is None):
            self.Header = Node(d)
            self.Current = self.Header
        else:
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp
    def insertCurrentNext(self,d):
        '''
        insertCurrentNext method sets new Node as the next node after the current node
        Parameters:
            self, data of new node
        Returns:
            None
        '''
        if (self.Header is None):
            self.Header = Node(d)
            self.Current = self.Header
        else:
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp
    def removeBeginning(self):
        '''
        removeBeginning method removes current Header by setting the node after the header in the list as the new header
        Parameters:
            self
        Returns:
            returns data of node removed
        '''
        if (self.Header is None):
            return None
        else:
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans
    def removeCurrentNext(self):
        '''
        removeCurrentNext method removes node after the current node
        Parameters:
            self
        Returns:
            returns data of node removed
        '''
        if (self.Current.Next is None):
            return None
        else:
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans
    def nextCurrent(self):
        '''
        nextCurrent method sets the next node as the current node
        Parameters:
            self
        Returns:
            None
        '''
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header
    def resetCurrent(self):
        '''
        resetCurrent method sets the header as the current node
        Parameters:
            self
        Returns:
            None
        '''
        self.Current = self.Header
    def getCurrent(self):
        '''
        getCurrent method returns data of current node
        Parameters:
            self
        Returns:
            returns data of current node
        '''
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None
    def printList(self, msg="====="):
        '''
        printList method prints the data of the nodes of the linked list in order and the data of the current node separately
        Parameters:
            self, msg(str)
        Returns:
            None, prints list data and current node data to console
        '''
        p = self.Header
        print("=====",msg)
        while (p is not None):
            print(p.Data, end=" ")
            p = p.Next
        if (self.Current is not None):
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")
        

def main():
    '''
    main function creates linked list from data and allows user to input data to be added to or rmeoved from sorted list
    Parameters:
        None
    Returns:
        None, prints data of linked list
    '''
    print("This program creates linked list from pre-existing data.")
    print("You may repeatedly enter integer values to change the list.")
    print("Enter an integer that does not exist in the list to add that integer to the sorted list.")
    print("Enter an integer that already exists in the list to remove it.")
    print("Enter -1 to quit the program.")
    #Intialize myArray as empty list
    myArray = []

    #Access data from txt file and add it to myArray list
    myFileData = open("data.txt", "r")
    for line in myFileData:
        myArray.append(eval(line))
    
    #sort data and reverse so array is in descending order
    myArray.sort()
    myArray.reverse()

    #Create linked list from data and print for user to see
    myList = LinkedList()
    for x in myArray:
        myList.insertBeginning(x)
    myList.printList()

    #Create infinite loop for user to repeatedly enter values
    while True:
        userValue = eval(input("Enter integer value to be either added or removed from Linked List: "))
        myList.resetCurrent()
        #quit program if user enters -1
        if userValue == -1:
            break
        else:
            #loop through the linked list until user value is appropriately handled
            while True:
                #remove Header if user value is equal to its data
                if myList.Header.Data == userValue:
                    myList.removeBeginning()
                    myList.printList()
                    break
                #insert value at last position of the list
                elif myList.Current.Next is None:
                    myList.insertCurrentNext(userValue)
                    myList.printList()
                    break
                #remove next after current if user value is equal to its data
                elif myList.Current.Next.Data == userValue:
                    myList.removeCurrentNext()
                    myList.printList()
                    break
                #insert user value into appropriate sorted position within the sorted list
                elif (myList.Current.Data <= userValue) and (myList.Current.Next.Data >= userValue):
                    myList.insertCurrentNext(userValue)
                    myList.printList()
                    break
                #change the current node to the next node
                else:
                    myList.nextCurrent()

#Call the main function        
main()