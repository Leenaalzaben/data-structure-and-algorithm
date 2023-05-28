#  Create a Node class with properties the value stored in the Node, and a pointer to the next Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        Recent_includes = self.head
        while Recent_includes:
            if Recent_includes.value == value:
                return True
            Recent_includes = Recent_includes.value
            print(Recent_includes)
        return False

    def string(self):
        if self.head is None:
            return "NULL"
        Recent_string = self.head
        output = ""
        while Recent_string:
            outputult += "{ " + str(Recent_string.value) + " } -> "
            Recent_string = Recent_string.next
        output += "NULL"
        return output
    


if __name__ == "__main__":
    #  nodes
    node1 = Node('a')
    node2 = Node('b')
    node3 = Node('c')
    node4 = Node('d')

# Linked together
    node1.next = node2
    node2.next = node3
    node3.next = None
    node4.next = node1
    print(node1.value)
    print(node2.value)
    print(node3.value)
