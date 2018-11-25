"""
Creating link lists out of Nodes in Python.
"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Get data of node:
    def get_value(self):
        return self.value

    # Get link of node:
    def get_next_node(self):
        return self.next_node

    # Set a new link between nodes:
    def set_next_node(self, next_node):
        self.next_node = next_node


# Linked list class:
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    # Get head node method:
    def get_head_node(self):
        return self.head_node

    # Insert new head node method:
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node


    # Presenting node method:
    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            string_list += str(current_node.value) + "\n"
            current_node = current_node.get_next_node()
        return string_list


    # Removing node method:
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node

ll = LinkedList("Original head node")
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())


# Linked Lists Analyzed: —————————————————————————————————————————————————————>
"""
No need to import Node from _1_nodes.py file because we already have it here.
Linked lists are created out of nodes, so first a Node class is created.
"""
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Get data of node:
    def get_value(self):
        return self.value

    # Get link of node:
    def get_next_node(self):
        return self.next_node

    # Set a new link between nodes:
    def set_next_node(self, next_node):
        self.next_node = next_node


"""
Below is a LinkedList class. We use the nodes to create the linked list.
The composition of linked list are nodes linked togheter from head node to
the last node.
"""
# Linked list class:
class LinkedList:
    """
    We define the __init__ of the LinkedList class as folows:
    - self i.e. the instance.
    - value, which is the data of the instance. This data's default is None.
    meaning no data at all.
    """
    def __init__(self, value=None):
        """
        Then we have a variable called head_node which is the first node in a
        linked list. Head node is defined as an instance of the Node class
        with a value; value is set to None.
        """
        self.head_node = Node(value)

        """
        the get_head_node function returns the head_node of an instance.
        """
    # Get head node method:
    def get_head_node(self):
        return self.head_node

        """
        the insert_beginning is an important function for linked lists, that allow
        one to insert a new node into an instnace of a linked list.
        Meaning that the inserted node becomes the new head node.
        """
    # Insert new head node method:
    def insert_beginning(self, new_value):
        """
        define a variable as new_node being an instance of the Node class with
        a value defined as new_value. This is where the node data goes.
        """
        new_node = Node(new_value)
        """
        With the 'set_next_node' function we link the new_node with the
        current head_node of the instance. This should look like this:
        (new_node) --> (head_node). Thus, creating a link.
        """
        new_node.set_next_node(self.head_node)
        """
        Now we say that that link:
        (new_node) --> (head_node) should become the new head_node of the
        instance.  Meaning that the head node is now the new_node, with the previous
        head_node being the second node now. Adding new nodes is thus the same
        as creating a new link on top of the current head node.
        """
        self.head_node = new_node


        """
        This class method turns the current linked list into strings, so that
        we may see them with our eyes.
        """
    # Presenting node method:
    def stringify_list(self):
        """
        Here we have a variable that contains an empty string.
        The variable is called string_list.
        """
        string_list = ""
        """
        Her we define our starting node in the variable named current_node.
        The current_node variable is set to the head_node of the instance this
        function is being called on/from.
        """
        current_node = self.head_node
        """
        A while loop saying to continue the loop until
        current_node returns None?
        __________________________________________________________
        Example iteration:

        1) current_node = 'ffg'
        2) current_node = 'A'
        3) current_node = 'Q'
        4) current_node = 'X'
        5) current_node = 'F'
        """
        while current_node:
            """
            Below it says to attach the current_node's value in string format
            to the string_list variable. And also add a '-->'.
            And it says to keep doing this until the 'get_next_node' function cannot
            call the next node since it has reached the end of the line.
            __________________________________________________________
            Example iteration:

            1) string_list += 'ffg--> '
            2) string_list += 'ffg--> A--> '
            3) string_list += 'ffg--> A--> Q--> '
            4) string_list += 'ffg--> A--> Q--> X--> '
            5) string_list += 'ffg--> A--> Q--> X--> F--> '
             F points to no new node meaning the loop ends.
            """
            string_list += str(current_node.value) + "--> "
            """
            Then it changes the variable called current_node to the next node.
            The next node is gotten by using the get_next_node method from the Node
            class. The method is used on the current_node. And since it is being used
            it on it, the current_node is always the next in line of the current
            current_node.
            __________________________________________________________
            Example iteration:

            1) current_node = ffg.A  (the node that links to the next node in line)
            2) current_node = A.Q
            3) current_node = Q.X
            4) current_node = X.F
            5) current_node = F.None (Where the while loop stops!)
            """
            current_node = current_node.get_next_node()

            """
            After the loop has reached the end of the linked list, it returns
            a string showing all of the nodes and the data they carry in the linked
            list the function has been called on.
            """
        return string_list


    # Removing node method:
    """
    Removing a Node from a link is much trickier since it requires the link
    to first link to the node next in line before removal.
    Remove node has instance, and value_to_remove as parameters.
    value_to_remove is the Node that needs to be removed.
    """
    def remove_node(self, value_to_remove):
        """
        First a variable that contains the head_node of the ll instance called
        current_node.
        """
        current_node = self.head_node
        """
        Then we have a conditional branch checking if the value of the current
        node(head_node) is the same as the node we want to remove.
        If that is the case, it is much easier to remove the node:
        """
        if current_node.get_value() == value_to_remove:
            """
            If the node to be removed is the same as the head node. Then we change
            the content of the head_node from the specific ll instance .
            In this case the head_node becomes the next node in line .
            For example:
            ffg--> A--> Q--> x--> F-->
            Head node ffg becomes head node A.  Because
            ffg = ffg.A / A
            """
            self.head_node = current_node.get_next_node()
        else:
            """
            If the condition is not met. Code goes into a while loop.
            The while loop works the same as the previous while loop in the stringify
            method.
            """
            while current_node:
                """
                next_node variable is defined as the link of the current_nodes.
                meaning A because ffg.A = A.
                """
                next_node = current_node.get_next_node()
                """
                Here it checks if A is equal to the value_to_remove.
                """
                if next_node.get_value() == value_to_remove:
                    """
                    If so. Then it says
                    """
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node


ll = LinkedList("F")        # > Current tail node.
ll.insert_beginning("X")
ll.insert_beginning("Q")
ll.insert_beginning("A")
ll.insert_beginning("ffg")  # > Current head node.
print(ll.stringify_list())

Produces:
ffg--> A--> Q--> X--> F-->
