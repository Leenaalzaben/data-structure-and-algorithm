class Node:
    """
    Class representing a node in a linked list.
    """
    def __init__(self,value=None,next=None):
         """
        Initialize a new node with the given value and next node reference.

        Args:
            value: The value to be stored in the node.
        next: Reference to the next node.
         """
         self.value = value
         self.next = next
   

class Queue:
    """
          Class representing a queue implemented using a linked list.
     """
    
    def __init__(self, front=None, back=None):
        """
        Initialize a new queue with the given front and back nodes.

        Args:
            front: The first node in the queue.
            back: The last node in the queue.
        """
        self.front = front
        self.back = back

    def  enqueue(self,value) :
        """
        Add an element to the back of the queue.

        Args:
            value: The value to be added to the queue.
        """
        node = Node(value)
        #check if queue is empty:
        if self.front is None:
         # If the queue is empty, set the front and back nodes to the new node.
            self.front=node
            self.back=node
        # TODO
        # if not :
        else:   
        # Otherwise, add the new node to the back of the queue and update the back node reference.
  
         self.back.next= node
         self.back = node 

    def dequeue(self):
        def dequeue(self):
         """
        Remove and return the element at the front of the queue.

        Returns:
            The value of the dequeued element.
        
        Raises:
            Exception: If the queue is empty.
         """
        #check if queue is empty:
        if self.front is None:
            raise Exception("Qoueue is empty")
        temp = self.front
        value =temp.value
        self.front=temp.next
        # TODO
        #if not:
        if temp is None:
        # If the queue had only one element, update the back node reference to None.

            self.back=None
        return value    
        
        
        # self.front = temp.next
        # temp.next = None
        # return temp.value
    def peek(self):
        """
        Get the value of the element at the front of the queue without removing it.

        Returns:
            The value of the element at the front of the queue.
        
        Raises:
            Exception: If the queue is empty.
        """
        if self.front is None:
            raise Exception("Queue is empty") 
        return self.front.value   
    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None
    

    def __str__(self):
        """
        Return a string representation of the queue.

        Returns:
            A string representation of the queue.
        """
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"   


if __name__ == "__main__":
    q=Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    print(q)
    print(q.front.value)
    print(q.back.value)
    print("deleted element is ",q.dequeue())#deleted node value
    print(q)
    print(q.front.value)
    print(q.back.value)




