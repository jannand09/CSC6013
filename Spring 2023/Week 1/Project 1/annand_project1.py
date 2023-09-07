# Create linked list with data from txt file
# and allow user to insert/delete data from linked list

class Node:
    def __init__(self, d):
        """
        Node class constructor initializes Node, the data associated with node, and the next value
        Parameters:
            self, data of Node
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
            self, data of new Node
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
        if self.Header is None:
            self.Header = Node(d)
            self.Current = self.Header
        else:
            tmp = Node(d)
            tmp.Next = self.Header
            self.Header = tmp

    def insertCurrentNext(self, d):
        """
        insertCurrentNext method sets new Node as the next node after the current node
        Parameters:
            self, data of new node
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
        printList method prints the data of the nodes of linked list in order and the data of the current node
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
        if self.Current is not None:
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")


def create_array(file):
    """
    Creates array using data from txt file
    Parameters:
        txt file
    Returns:
        Array
    """
    array = []
    file_data = open(file, "r")
    for line in file_data:
        array.append(eval(line))
    return array


def array_to_list(array):
    """
    Converts array into linked list with data in numerical order
    Parameters:
        array
    Returns:
        Linked List
    """
    array.sort()
    array.reverse()
    new_list = LinkedList()
    for x in array:
        new_list.insertBeginning(x)
    return new_list


def main():
    """
    Creates linked list from data and allows user to input data to be added to or removed from sorted list
    Returns:
        None, prints data of linked list
    """
    print("This program sorts pre-existing data and stores it in a linked list.")
    print("You may enter integer values to change the list.")
    print("Enter an integer that does not exist in the list to add that integer to the sorted list.")
    print("Enter an integer that already exists in the list to remove it.")
    print("Enter -1 to quit the program.")

    my_array = create_array("list_data.txt")
    my_list = array_to_list(my_array)

    # Create loop for user to repeatedly enter values
    while True:
        my_list.resetCurrent()
        my_list.printList()

        user_value = eval(input("Enter integer value to be either added or removed from Linked List: "))

        # quit program if user enters -1
        if user_value == -1:
            break
        else:
            # loop through the linked list until user value is appropriately handled
            while True:
                # remove Header if user value is equal to its data
                if my_list.Header.Data == user_value:
                    my_list.removeBeginning()
                    my_list.printList()
                    break
                # insert value at last position of the list
                elif my_list.Current.Next is None:
                    my_list.insertCurrentNext(user_value)
                    my_list.printList()
                    break
                # remove next after current if user value is equal to its data
                elif my_list.Current.Next.Data == user_value:
                    my_list.removeCurrentNext()
                    my_list.printList()
                    break
                # insert user value into appropriate sorted position within the sorted list
                elif (my_list.Current.Data <= user_value) and (my_list.Current.Next.Data >= user_value):
                    my_list.insertCurrentNext(user_value)
                    my_list.printList()
                    break
                # change the current node to the next node
                else:
                    my_list.nextCurrent()


# Call the main function
main()
