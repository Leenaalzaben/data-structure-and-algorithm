from linkedListImplementation.LinkedList import LinkedList
import unittest

class test_Linked_List(unittest.TestCase):
    # Organize a LinkedList 
    def setUp(self):
        self.list = LinkedList()


    # test One insert method
    def test_insert(self):
        self.list.insert('a')
        self.list.insert('b')
        self.list.insert('c')

    

    # Test Two includes
    def test_includes(self):
       
        self.list.insert('c')
        self.list.insert('b')
        self.list.insert('a')
        
    #  Test String
    def test_string(self):
    
        self.list.insert('a')
        self.list.insert('b')
        self.list.insert('c')
           




if __name__ == '__main__':
    unittest.main()
