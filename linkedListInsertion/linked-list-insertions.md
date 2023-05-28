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
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    def insertBefore(self, value, newValue):
        if self.head is None:
            return

        if self.head.value == value:
            new_node = Node(newValue)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            if n.next.value == value:
                break
            n = n.next

        if n.next is None:
            return

        new_node = Node(newValue)
        new_node.next = n.next
        n.next = new_node

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp:
            if temp.value == value:
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next
            def kth_from_end(self, k):
        if k <= 0:
            return None
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        if k > length:
            return None
        location = length - k
        current = self.head
        for i in range(location):
            current = current.next

        return current.value


       

            ```
