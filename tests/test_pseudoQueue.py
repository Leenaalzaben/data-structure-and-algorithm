import pytest
from StackAndQueue.PseudoQueue import PseudoQueue
from StackAndQueue.stack import Stack


@pytest.fixture
def pseudo_queue():
    return PseudoQueue()

def test_enqueue(pseudo_queue):
    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(2)
    pseudo_queue.enqueue(3)
    assert str(pseudo_queue) == "1 -> 2 -> 3"


def test_dequeue(pseudo_queue):
    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(2)
    pseudo_queue.enqueue(3)
    assert pseudo_queue.dequeue() == 1
    assert pseudo_queue.dequeue() == 2
    assert pseudo_queue.dequeue() == 3
    with pytest.raises(IndexError):
        pseudo_queue.dequeue()

def test_str_representation_empty_queue(pseudo_queue):
    assert str(pseudo_queue) == "Empty PseudoQueue"

def test_repr_representation_empty_queue(pseudo_queue):
    assert repr(pseudo_queue) == "Empty PseudoQueue"
