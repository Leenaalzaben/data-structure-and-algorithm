
import pytest
from linkedListInsertion.insertionLinkedList import Node,LinkedList


def test_empty_list():
    actual = LinkedList().head
    expected = None
    assert actual == expected


def test_insert_in_list():
    link_list = LinkedList()
    link_list.insert(75)
    actual = link_list.head.value
    expected = 75
    assert actual == expected


def test_append_node_to_list():
    link_list = LinkedList()
    link_list.insert('b')
    link_list.insert('c')
    link_list.append('a')
    actual = str(link_list)
    expected = "{c}->{b}->{a}->None"
    assert actual == expected

def test_append_nodes_to_list():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    actual = str(link_list)
    expected = "{d}->{c}->{b}->{a}->None"
    assert actual == expected

def test_insert_before_middle():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insert_before('b', 'middle')
    actual = str(link_list)
    expected = "{d}->{c}->{middle}->{b}->{a}->None"
    assert actual == expected


def test_insert_after_middle():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
 

def test_insert_before_first():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
  

def test_insert_after_last():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insert_after('a', 'last')
    actual = str(link_list)
    expected = "{d}->{c}->{b}->{a}->{last}->None"
    assert actual == expected

def test_list_head():
    node = Node(45)
    actual = LinkedList(node).head
    expected = node
    assert actual == expected

def test_insert_multiple_nodes():
    linked_list = LinkedList("a")
    linked_list.insert("b")
    linked_list.insert("c")
    linked_list.insert("d")
    actual = linked_list.head.value
    expected = 'd'
    assert actual == expected

def test_if_list_includes_two():
    node = Node(50)
    actual = LinkedList(node).includes(49)
    expected = False
    assert actual == expected


def test_list_includes_onehundred():
    node = Node(100)
    actual = LinkedList(node).includes(100)
    expected = True
    assert actual == expected


def test_linked_list_str():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('b')
    link_list.insert('a')



def test_kth_greater_than_len():
     link_list = LinkedList()
     link_list.insert(1)
     link_list.insert(2)
     link_list.insert(3)
     link_list.insert(4)
     with pytest.raises(Exception):
      link_list.kthFromEnd(5)
    
def test_kth_equal_to_ll_length():
    link_list = LinkedList()
    link_list.insert(1)
    link_list.insert(2)
    link_list.insert(3)
    link_list.insert(4)
    with pytest.raises(Exception):
        link_list.kthFromEnd(4)

def test_kth_negative():
    link_list = LinkedList()
    link_list.insert(1)
    link_list.insert(2)
    link_list.insert(3)
    link_list.insert(4)
    with pytest.raises(Exception):
        link_list.kthFromEnd(-4)

def test_kth_size_one():
    link_list = LinkedList()
    link_list.insert(1)
    actual = link_list.kthFromEnd(0)
    expected = 1
    assert actual == expected

def test_kth_middle_value():
    link_list = LinkedList()
    link_list.insert(10)
    link_list.insert(15)
    link_list.insert(20)
    link_list.insert(25)
    link_list.insert(30)

def test_zip_Lists():
    linkedlist1 = LinkedList()
    linkedlist1.insert(1)
    linkedlist1.insert(2)
    linkedlist1.insert(3)
    linkedlist1.insert(4)

    linkedlist2 = LinkedList()
    linkedlist2.insert(9)
    linkedlist2.insert(8)
    linkedlist2.insert(7)
    linkedlist2.insert(6) 