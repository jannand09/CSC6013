class Person:
    def __init__(self, name, family_name, age):
        """
        Person class constructor initializes name, surname, and age of Person object
        Parameters:
            self, name(str), family_name(str), age(int)
        Returns:
            None
        """
        self.name = name
        self.famN = family_name
        self.age = age

    def getName(self):
        """
        getName method returns the first name of the Person object
        Parameters:
            self
        Returns:
            self.name (str)
        """
        return self.name

    def getFullName(self):
        """
        getFullName returns string of the first name and family name of the Person object instance
        Parameters:
            self
        Returns:
            self.name and self.famN with space in between (str)
        """
        return self.name + " " + self.famN

    def getFamilyName(self):
        """
        getFamily Name method returns the surname name of the Person object
        Parameters:
            self
        Returns:
            self.famN (str)
        """
        return self.famN

    def getAge(self):
        """
        getAge method returns the age of the Person object
        Parameters:
            self
        Returns:
            self.age (int)
        """
        return self.age


class Node:
    def __init__(self, d):
        """
        Node class constructor initializes Node, the data associated with node, and the next value
        Parameters:
            self, d(any)
        Returns:
            None
        """
        self.Data = d
        self.Next = None


class LinkedList:
    def __init__(self, d=None):
        """
        LinkedList class constructor initializes Header as None or Node(d) and Current as None or Header
        Parameters:
            self, d(any)
        Returns:
            None
        """
        if d is None:
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header

    def insertBeginning(self, d):
        """
        insertBeginning method sets new Node as header of the linked list
        Parameters:
            self, data of new node
        Returns:
            None
        """
        if self.Header is not None:
            tmp = Node(d)
            tmp.Next = self.Header
            self.Header = tmp
        else:
            self.Header = Node(d)
            self.Current = self.Header

    def insertCurrentNext(self, d):
        """
        insertCurrentNext method sets new Node as the next node after the current node
        Parameters:
            self, d(any)
        Returns:
            None
        """
        if self.Header is None:
            self.Header = Node(d)
            self.Current = self.Header
        else:
            tmp = Node(d)
            tmp.Next = self.Current.Next
            self.Current.Next = tmp

    def removeBeginning(self):
        """
        removeBeginning method removes current Header by setting the node after the header in the list as the new header
        Parameters:
            self
        Returns:
            returns data of node removed
        """
        if self.Header is None:
            return None
        else:
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans

    def removeCurrentNext(self):
        """
        removeCurrentNext method removes node after the current node
        Parameters:
            self
        Returns:
            returns data of node removed
        """
        if self.Current.Next is None:
            return None
        else:
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans

    def nextCurrent(self):
        """
        nextCurrent method sets the next node as the current node
        Parameters:
            self
        Returns:
            None
        """
        if self.Current.Next is not None:
            self.Current = self.Current.Next
        else:
            self.Current = self.Header

    def resetCurrent(self):
        """
        resetCurrent method sets the header as the current node
        Parameters:
            self
        Returns:
            None
        """
        self.Current = self.Header

    def getCurrent(self):
        """
        getCurrent method returns data of current node
        Parameters:
            self
        Returns:
            returns data of current node
        """
        if self.Current is not None:
            return self.Current.Data
        else:
            return None

    def printList(self, msg="====="):
        """
        printList method prints the data of the nodes of the linked list in order
        and the data of the current node separately
        Parameters:
            self, msg(str)
        Returns:
            None, prints list data and current node data to console
        """
        p = self.Header
        print("=====", msg)
        while p is not None:
            print(p.Data, end=" ")
            p = p.Next
        if self.Current is None:
            print("Empty Linked List")
        else:
            print("Current:", self.Current.Data)


def main():
    """
    main method creates a Stack as an instance of Linked List object filled of Person object instances
    from data from CSV file and allows user to remove up to 4 items from the stack at a time
    Returns:
        None, prints feedback to user or data from current object at the top of the stack
    """
    # Create stack as an instance of LinkedList object
    my_stack = LinkedList()
    # initialize counter to keep track of number of people in stack
    data_counter = 0

    # Get data from CSV file
    my_file_data = open("annand_project2_names.csv", "r")
    # Add data from each line of file to stack as instance of Person object and so that last in is at the top
    for line in my_file_data:
        data = line.split(",")
        my_stack.insertBeginning(Person(data[0], data[1], int(data[2])))
        data_counter += 1

    # Create infinite loop
    while True:
        # Set current as the Header
        my_stack.resetCurrent()
        # Tell user how many people are in the stack and ask how many to remove
        print("There are ", str(data_counter), " people in the stack.")
        print("Enter 0 to quit the program.")
        user_input = input("Enter the amount of data points to be removed from the stack up to 4: ")
        try:
            remove_amt = eval(user_input)
        except NameError:
            print("Please enter an integer value.")
            continue
        except ValueError:
            print("Please enter an integer value.")
            
            continue

        # Quit program if user enters 0
        if remove_amt == 0:
            break
        # Ensure that user submits a valid number to remove from the list
        elif remove_amt > data_counter:
            print("There are not enough people left in the stack to remove that many.")
        elif remove_amt > 4 or remove_amt < 1:
            print("Please enter an integer between 1 and 4.")
        # Remove people from the top of the stack according to user input
        else:
            for x in range(remove_amt):
                my_stack.removeBeginning()
            if my_stack.getCurrent() is None:
                break
            else:
                # print information of the person at the top of the stack
                print("Person at the top of the stack: ")
                print(my_stack.getCurrent().getFullName())
                print("Age: ", str(my_stack.getCurrent().getAge()))
                data_counter = data_counter - remove_amt


main()
