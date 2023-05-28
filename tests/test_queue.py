import pytest
from StackAndQueue.queue import Queue

def test_enqueue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

def test_dequeue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(15)
    q.enqueue(20)
    q.enqueue(25)
    q.enqueue(30)

def test_peek():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    

def test_is_empty():
    q = Queue()
    # q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    

def test_instance():
    q = Queue()

def test_dequeue_Exeptions():
    q=Queue()
    with pytest.raises(Exception):
        q.dequeue()

def test_enqueue_Exeptions():
    q=Queue()
    with pytest.raises(Exception):
        q.enqueue() 
def test_peek_Exeptions():  
    q = Queue()
    with pytest.raises(Exception):
        q.peek()             