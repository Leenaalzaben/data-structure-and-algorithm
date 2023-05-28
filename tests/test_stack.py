import pytest
from StackAndQueue.stack import stack

def test_push_stack():
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)

def test_pop_stack():
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
   
def test_empty():
    s = stack()
    s.push(1)

def test_peek():
    s = stack()
    s.push(1)
  

def test_instance():
    s = stack()
def test_push_Exeption():
    s = stack()
    with pytest.raises(Exception):
        s.push()
def test_pop_Exeption():
    s = stack()
    with pytest.raises(Exception):
        s.pop()
def test_peek_Exeption():
    s = stack()
    with pytest.raises(Exception):
        s.peek()


