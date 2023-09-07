
class Person:
    def __init__(self, name, familyName, age):
        '''
        Person class constructor intializes name, surname, and age of Person object
        Parameters:
            self, name, last name, age
        Returns:
            None
        '''
        self.name = name
        self.famN = familyName
        self.age = age
    def getName(self):
        '''
        getName method returns the first name of the Person object
        Parameters:
            self
        Returns:
            self.name (str)
        '''
        return self.name
    def getFullName(self):
        '''
        getFullName returns string of the first name and family name of the Person object instance
        Parameters:
            self
        Returns:
            sel.fname and self.famN with space in between (str)
        '''
        return self.name+" "+self.famN
    def getFamilyName(self):
        '''
        getFamily Name method returns the surname name of the Person object
        Parameters:
            self
        Returns:
            self.famN (str)
        '''
        return self.famN
    def getAge(self):
        '''
        getAge method returns the age of the Person object
        Parameters:
            self
        Returns:
            self.age (int)
        '''
        return self.age

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
    main method creates a Stack as an instance of Linked List object filled of Person object instances from data from CSV file a
        and allows user to remove up to 4 itesm from the stack at a time
    Parameters:
        None
    Returns:
        None, prints feedback to user or data from current objetc at the top of the stack   
    '''
    #Create stack as an instance of LinkedList object
    myStack = LinkedList()
    #initialize counter to keep track of number of people in stack
    data_counter = 0
    
    #Get data from CSV file
    myFileData = open("annand_project2_names.csv", "r")
    #Add data from each line of file to stack as instance of Person object and so that last in is at the top
    for line in myFileData:
        data = line.split(",")
        myStack.insertBeginning(Person(data[0], data[1], int(data[2])))
        data_counter += 1

    #Create infinte loop
    while True:
        #Tell user how many people are in the stack and ask how many to remove
        print("There are ",str(data_counter)," people in the stack.")
        user_input = eval(input("Enter the amount of data points to be removed from the stack up to 4: "))
        #Set current as the Header
        myStack.resetCurrent()
        #Ensure that user submits a valid number to remove from the list
        if user_input > data_counter:
            print("There are not enough people left in the stack to remove that many.")
        elif user_input > 4 or user_input < 1:
            print("Please enter an integer between 1 and 4.")
        #Remove people from the top of the stack according to user input
        else:
            for x in range(user_input):
                myStack.removeBeginning()
            if myStack.getCurrent() is None:
                break
            else:
                #print information of the person at the top of the stack
                print("Person at the top of the stack: ")
                print(myStack.getCurrent().getFullName())
                print("Age: ",str(myStack.getCurrent().getAge()))
                data_counter = data_counter - user_input

main()
        

