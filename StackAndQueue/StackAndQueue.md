# Challenge Title: Stack and Queue 

## Stack Implementation

This section demonstrates the implementation of a Stack data structure in Python.

## Queue Implementation

This section illustrates the implementation of a Queue data structure, also in Python.

## Approach & Efficiency

The **Stack implementation** achieves O(1) time complexity for the following operations:

- push
- pop
- peek
- is_empty

The **Queue implementation** achieves O(1) time complexity for the following operations:

- enqueue
- dequeue

Both the stack and queue implementations have a space complexity of O(n), where n is the number of elements in the stack or queue.

## Solution

### Tests

To run the tests, execute the following commands:
<br>
`pytest tests/test_stack.py`<br>
`pytest tests/test_queue.py`

### Running the Code 
[Stack](../Stack/stack.py)<br>
[Queue](./queue.py)

To run the code, execute the following commands:<br>
`python3 Queue/queue.py`<br>
`python3 Stack/stack.py`

1. What are you testing?What should it do?
   What is the actual output?What is the expected output?

    Test: Stack - Push a value onto the stack
     Description: Tests the push() method of the Stack class to ensure that a value is successfully pushed onto the stack.
    Stack State: [2, 1] -> [top]
    Action: stack.push(3)
    Stack State: [3, 2, 1] -> [top]
    Expected Output: The stack should contain [3, 2, 1] with the top pointing to the node containing 3.

    <!-- ****************************************** -->

## PseudoQueue
