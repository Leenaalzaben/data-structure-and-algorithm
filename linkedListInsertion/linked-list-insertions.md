# Challenge_Class_06||  Linked List Insertions

The Linked List (LL) class have three methods which the first for append, the second for insert_before, and last one for insert_after
The append method focuses on extending the linked list by adding a new node to the end.
The Insert_before method deals with inserting a new node before the first occurrence of a specified value in the list.
The  Insert_after method involves inserting a new node after the first occurrence of a specified value in the list.
Also The The next one is represents a method called "kth_from_end" within a class. It takes an input parameter "k," which represents the position from the end of the linked list. The method aims to find and return the value of the node at the specified position.

## Whiteboard Process

### Linked List Insertions _ Append

![Miro](./miroL.png)

### Linked List Insertions _ Before

![Miro](./miro2.png)

### Linked List Insertions _ After

![Miro](./MiroP.png)

### Linked List kth_from_end

![LinkedListkth](./LinkedListkth.png)

## Approach & Efficiency

### Linked List Insertions _Append

The approach is to create a new node with the new_value and traverse the linked list

### Linked List Insertions_ Before

The approach is to traverse the linked list, find the node with value, and insert the new node before it.

### Linked List Insertions _ After

The approach is to traverse the linked list, find the node with value, and insert the new node after it

### Linked List kth_from_end

The approach ensures that the desired position is within bounds, calculates the location efficiently, and returns the correct value. It has a time complexity of O(N) and handles edge cases appropriately.

## Big O

### Linked List Insertions _ Append

**Time complexity** Since there is a loop from head to end, the function does O(n) work
This method can also be optimized to work in O(1) by keeping an extra pointer to the tail of the linked list.<br>
**Space complexity** The space complexity is O(1) or constant space because the memory used does not depend on the size of the input data or the length of the linked list.

### Linked List Insertions _ Before

**Time complexity** of the insertBefore algorithm in the provided code snippet is O(n), where n is the number of nodes in the linked list.

**The space complexity** of the insertBefore algorithm in the provided code snippet is O(1), which means it requires constant space.

### Linked List Insertions _ After

**The time complexity** of the insert_after method in the given code snippet is O(n), where n is the number of nodes in the linked list.

**The space complexity** of the insert_after method is O(1) because it uses a constant amount of additional space.

### Linked List kth_from_end

The time complexity of the kth_from_end method is dominated by the linear traversal to calculate the length of the linked list, resulting in a time complexity of O(N).

The space complexity of the algorithm is O(1) because it uses a constant amount of additional memory to store variables length, current, and location

## Solution

[Link](./inslinkedlist.py)

### Linked List Insertions _ Append

```python
 
class Node:

    def __init__(self, value, next=None):
      
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head=head
    def insert(self,value):
      
        node = Node(value)
        if self.head is not None:

            node.next = self.head

        self.head = node

    def includes(self,value):
       
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False
    

    def __str__(self):
      

        current = self.head
        str = ''

        while current is not None:
            str += f"{{{current.value}}}->"
            current = current.next
        return str + 'None'
    
    def append(self, value):
           
        node = Node(value)
        current = self.head
        if self.head == None:
            self.head = node
            return

        while current.next is not None:
            current = current.next

        current.next = node
    def insert_before(self,value,new_value):
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
    
        current = self.head
        counter = []
        while current is not None:
            counter.append(current)
            current = current.next
        length_ = len(counter)

        if k < 0 :
            raise Exception ('Negative value not accepted')
        elif k < length_:
            return counter[length_ - (k+1) ].value
        else:
         raise Exception('There is no value at that index!')
        
            ```
