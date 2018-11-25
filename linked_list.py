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
