# Create a binary tree from values in a txt file and convert them to directed adjacency matrix in which difference between
# data values of parent and child nodes is equal to weight of edges between vertices

class Node:
    def __init__(self, d):
        """
        constructor function creates instance of Node
        :param d: int value
        :returns: none
        """
        self.Data = d
        self.Left = None
        self.Right = None


class Tree:
    def __init__(self, d=None):
        """
        constructor function creates instance of Tree and initializes Root
        :param d: int value or None
        :returns:
        """
        if d is None:
            self.Root = None
        else:
            self.Root = Node(d)

    def insert(self, d):
        """
        insert function inserts value in appropriate position in binary tree
        :param d: value to be inserted into tree (int)
        :returns:
        """

        def __insertHere__(n, data):
            """
            __insertHere__ function checks if value can be inserted as child of current node
            or continue to the next level of tree
            :param n: current node of Tree (obj: Node)
            :param data: value to be inserted into tree (int)
            :return:
            """
            # check if data is less than data of node
            if n.Data > data:
                if n.Left is None:
                    n.Left = Node(data)
                # recursively traverse tree if data cannot be placed as child of current node
                else:
                    __insertHere__(n.Left, data)
            # check if data is less than data of node
            elif n.Data < data:
                if n.Right is None:
                    n.Right = Node(data)
                # recursively traverse tree if data cannot be placed as child of current node
                else:
                    __insertHere__(n.Right, data)

        # if root is none set root as node obj with data d
        if self.Root is None:
            self.Root = Node(d)
        else:
            # Check if d is less than data of root
            if self.Root.Data > d:
                if self.Root.Left is None:
                    self.Root.Left = Node(d)
                else:
                    __insertHere__(self.Root.Left, d)
            # check if d is greater than data of root
            elif self.Root.Data < d:
                if self.Root.Right is None:
                    self.Root.Right = Node(d)
                else:
                    __insertHere__(self.Root.Right, d)

    def check(self, d):
        """
        check if d is in the tree
        :param d: value to be checked for (int)
        :return: Boolean
        """
        def __check__(n, data):
            """
            check if data is at current node n and recursively traverse tree if
            current node is not a leaf
            :param n:
            :param data:
            :return:
            """
            if n is None:
                return False
            elif n.Data == data:
                return True
            elif n.Data > data:
                return __check__(n.Left, data)
            elif n.Data < data:
                return __check__(n.Right, data)

        return __check__(self.Root, d)

    def printInorder(self):
        """
        printInorder prints data of all nodes of tree in order
        :return: prints tree values in order
        """
        def __visit__(n):
            """
            __visit__ function recursively traverse all nodes to left of n and prints values,
            prints data of n and then recursively traverses all nodes to right of n and prints values
            :param n:
            :return: prints value of n
            """
            if n is not None:
                __visit__(n.Left)
                print(n.Data, end=" ")
                __visit__(n.Right)

        print("\n--------")
        __visit__(self.Root)
        print("\n--------")

    def printPreorder(self):
        """
        printPreorder prints data of all nodes of tree in preorder
        :return: prints tree values in preorder
        """
        def __visit__(n, h):
            """
            __visit__ function prints data of n , recursively traverses all nodes to left of n and prints values,
            and then recursively traverses all nodes to right of n and prints values
            :param n:
            :param h:
            :return: prints value of n
            """
            if n is not None:
                print("---" * h, n.Data)
                __visit__(n.Left, h + 1)
                __visit__(n.Right, h + 1)

        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")

    def printPostorder(self):
        """
        printPostorder prints data of all nodes of tree in postorder
        :return: prints tree values in postorder
        """
        def __visit__(n, h):
            """
            __visit__ recursively traverses all nodes to left of n and prints values,
            recursively traverses all nodes to right of n and prints values, and then function prints data of n
            :param n:
            :param h:
            :return: prints value of n
            """
            if n is not None:
                __visit__(n.Left, h + 1)
                __visit__(n.Right, h + 1)
                print("---" * h, n.Data)

        print("==========")
        __visit__(self.Root, 1)
        print("==========")

    def create_preorder_array(self):
        """
        create_preorder_array traverses the tree and returns list of values in preorder
        :return: preorder_list (list)
        """
        preorder_list = []

        def __visit__(n):
            """
            __visit__ function appends data of n to preorder_list, recursively traverses all nodes to left of n and appends values,
            and then recursively traverses all nodes to right of n and appends values
            :param n: Node (obj)
            :return:
            """
            if n is not None:
                preorder_list.append(n.Data)
                __visit__(n.Left)
                __visit__(n.Right)

        __visit__(self.Root)
        return preorder_list

    def create_node_preorder_dict(self):
        """
        create_node_preorder_dict traverses the tree and returns dictionary of key value pairs in which keys are data of each node 
        and values are lists of the data of the node's children; keys are in preorder
        :return: node_dict (dict)
        """
        node_dict = {}

        def __visit__(n):
            """
            __visit__ function updates node_dict and creates a key for the data of each node in the tree where
            each key has a list of the data of the children of the node; keys are in preorder in node_dict
            :param n: Node (obj)
            :return:
            """
            if n is not None:
                if n.Left is not None and n.Right is not None:
                    node_dict.update({n.Data: [n.Left.Data, n.Right.Data]})
                elif n.Left is None and n.Right is not None:
                    node_dict.update({n.Data: [None, n.Right.Data]})
                elif n.Left is not None and n.Right is None:
                    node_dict.update({n.Data: [n.Left.Data, None]})
                else:
                    node_dict.update({n.Data: [None, None]})
                __visit__(n.Left)
                __visit__(n.Right)

        __visit__(self.Root)
        return node_dict


def main():
    """
    main function creates an instance of the tree object using data from txt file and creates a list and a dictionary of
    data in tree; intializes a graph in the form of an adjacency matrix; iterate thorugh dictionary and 
    uses list to determine position at which to set new weight of the edge
    """
    # initialize instance of tree object
    my_tree = Tree()

    #insert values from txt file into tree
    numbers_file = open('numbers.txt', 'r')
    for line in numbers_file:
        my_tree.insert(eval(line))
    my_tree.printPreorder()

    # initialize list of data values from tree in preorder
    tree_list = my_tree.create_preorder_array()
    # create dictionary of nodes and their children data
    nodes = my_tree.create_node_preorder_dict()
    print("List of all data in tree in preorder: ", tree_list)
    print("Dictionary of tree data: ", nodes)

    # initialize adjacency matrix
    graph = [[0 for _ in range(len(tree_list))] for _ in range(len(tree_list))]

    # iterate through nodes(dict) keys
    for parent in nodes:
    # iterate through list of data of child nodes
        for child in nodes[parent]:
    # if parent node has child node, find appropriate position in adjacency matrix and set equal to absolute value of
    # difference between data of parent and dat of child node
            if child is not None:
                i = tree_list.index(parent)
                j = tree_list.index(child)
                graph[i][j] = abs(parent - child)

    print(graph)


main()
