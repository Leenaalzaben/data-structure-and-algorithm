class Node:
    """
    Class representing a node in a linked list.
    """

    def __init__(self, value=None, next=None):
        """
        Initialize a new node with the given value and next node reference.

        Args:
            value: The value to be stored in the node.
            next: Reference to the next node.
        """
        self.value = value
        self.next = next

class stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
        #TODO
        #check if the statck is empty or not 
        # stack its empty :
        if self.top is None:
            self.top=Node(value)
        else:  #IF NOT stack isn't empty :
            new_node =Node(value)
            new_node.next=self.top
            self.top=new_node


    def pop(self):
        #check if the stack is empty :
        #TODO raise an exception
        if self.top is None:
            raise Exception("Stack is empty")
        else:
         temp= self.top
         self.top = temp.next
         temp.next = None
        return temp.value

    def peek(self):
        #TODO
        if self.top is None:
            raise Exception("Stack is empty")
        else:
            return self.top.value

        
    def is_empty(self):
        #TODO
        #check if stack is empty-> True 
        if self.top is None:
            return True
        #if not -> False  Stack is not empty
        else:
            return False
        

    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"    


if __name__ ==  "__main__":
    stack_01= stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    print(stack_01)
    print(stack_01.top.value)