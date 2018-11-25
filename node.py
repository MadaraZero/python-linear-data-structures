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
