
class Node:
    """A node in a linked list."""

    def __init__(self, value, next=None):
        """
        Initialize a new node with a given value and next node.

        Args:
            value: The value to be stored in the node.
            next: The next node in the linked list.
        """
        self.value = value
        self.next = next



class LinkedList:
    """A linked list data structure."""
    def __init__(self, head=None):
        """
        Initialize a new linked list with a given head node.

        Args:
            head: The first node of the linked list.
        """
        
        self.head=head

    def insert(self,value):
        """
        Insert a new node with the given value at the beginning of the linked list.

        Args:
            value: The value to be inserted.
        """
        node = Node(value)
        if self.head is not None:

            node.next = self.head

        self.head = node

    def includes(self,value):
        """
        Check if the linked list contains a node with the given value.

        Args:
            value: The value to search for.

        Returns:
            True if the value is found, False otherwise.
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False
    

    def __str__(self):
        """
        Get a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """

        current = self.head
        str = ''

        while current is not None:
            str += f"{{{current.value}}}->"
            current = current.next
        return str + 'None'
    
    def append(self, value):
        """
        Append a new node with the given value at the end of the linked list.

        Args:
            value: The value to be appended.
        """
        node = Node(value)
        current = self.head
        if self.head == None:
            self.head = node
            return

        while current.next is not None:
            current = current.next

        current.next = node


    def insert_before(self,value,new_value):
        """
        Insert a new node with the given new value before the node with the specified value.

        Args:
            value: The value of the node before which the new node should be inserted.
            new_value: The value of the new node to be inserted.
        """

        current=self.head
        if current.value == value :
            self.insert(new_value)
            return
        
        while current is not None:
           if current.next.value == value :
               node = Node(new_value)
               node.next = current.next
               current.next = node

               return
           current=current.next


    def insert_after(self,value,new_value):
        """
        Insert a new node with the given new value after the node with the specified value.

        Args:
            value: The value of the node after which the new node should be inserted.
            new_value: The value of the new node to be inserted.
        """

        current=self.head
        if current.next.value == value :
            self.insert(new_value)
            return
        
        while current is not None:
           if current.value == value :
               node = Node(new_value)
               node.next = current.next
               current.next = node

               return
           current=current.next
    
    def kthFromEnd(self, k: int) -> int:
        """
        Find the value of the node that is k nodes from the end of the linked list.

        Args:
            k: The index of the node from the end (0-indexed).

        Returns:
            The value of the node.

        Raises:
            Exception: If the provided index is negative or greater than the length of the linked list.
        """
        current = self.head
        counter = []
        while current is not None:
            counter.append(current)
            current = current.next
        length_ = len(counter)

        if k < 0 :
            #  when the case  k =-1 raise exception
            raise Exception ('Negative value not accepted')
        elif k < length_:
            return counter[length_ - (k+1) ].value
        else:
         raise Exception('There is no value at that index!')
        
def zip_Lists(list1, list2):
    """
    Zips two linked lists together by alternating their elements.

    Parameters:
        list1 (LinkedList): The first linked list.
        list2 (LinkedList): The second linked list.
    """

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        next1 = current1.next
        next2 = current2.next
        current1.next = current2
        current2.next = next1
        last_current1 = current1.next
        current1 = next1
        current2 = next2
        if not current1 and current2:
            last_current1.next = current2

    return list1


if __name__ == "__main__":
    # Create instances of ll and nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Create the first ll
    linked_list1 = LinkedList(node1)
    node1.next = node2
    node2.next = node3

    # Create the second ll
    linked_list2 = LinkedList(node4)

    # Print the zipped ll
    zipped_list = zip_Lists(linked_list1, linked_list2)
    current_node = zipped_list.head
    while current_node:
        print(current_node.value)
        current_node = current_node.next
        
        

# if __name__=="__main__":
#     linkedlist = LinkedList()
#     linkedlist.insert(1)
#     linkedlist.insert(2)
#     linkedlist.insert(3)
#     linkedlist.insert(4)
  
#     print (linkedlist)
#     print(linkedlist.includes(3))
#     print(linkedlist.includes(11))
#     linkedlist.append(9)
#     linkedlist.append(8)
#     linkedlist.append(7)
#     linkedlist.append(5)
#     print(linkedlist)
#     linkedlist.insert_before(5,6)
#     print(linkedlist)
#     linkedlist.insert_after(1,2)
 
#     print(linkedlist)
#     print (linkedlist.kthFromEnd(1))
#     print (linkedlist.kthFromEnd(0))
#     # print (linkedlist.kthFromEnd(-1))
    

