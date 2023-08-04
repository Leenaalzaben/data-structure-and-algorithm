from hashtable.hashtable import HashTable
from hashmapRepeatedWord.hashmapRepeatedWord import repeated_word


def test_no_repeated_word():
    actual = repeated_word("This is just test brother, was ist das? ")
    expected = "no words found"
    assert actual == expected


def test_string_one():
    actual = repeated_word("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected


def test_string_two():
    actual = repeated_word(
        "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected = "it"
    assert actual == expected


def test_string_three():
    actual = repeated_word(
        "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    expected = "summer"
    assert actual == expected
import unittest
from TreeIntersection.treeIntersection import TreeNode, tree_intersection

class TestTreeIntersection(unittest.TestCase):

    def test_tree_intersection(self):
        # Test Case 1
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)
        tree1.left.left = TreeNode(4)
        tree1.left.right = TreeNode(5)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(3)
        tree2.right = TreeNode(6)
        tree2.left.left = TreeNode(4)
        tree2.left.right = TreeNode(7)

        result = tree_intersection(tree1, tree2)
        self.assertEqual(result, {1, 3, 4})

        # Test Case 2
        tree1 = TreeNode(10)
        tree1.left = TreeNode(5)
        tree1.right = TreeNode(30)
        tree1.left.left = TreeNode(1)
        tree1.left.right = TreeNode(7)

        tree2 = TreeNode(20)
        tree2.left = TreeNode(30)
        tree2.right = TreeNode(40)
        tree2.left.right = TreeNode(5)

        result = tree_intersection(tree1, tree2)
        self.assertEqual(result, {5, 30})

        # Add more test cases here...

if __name__ == '__main__':
from hashtable.hashtable import Node, LinkedList, HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_set_get(self):
        self.hash_table.set("key1", "value1")
        self.hash_table.set("key2", "value2")

        self.assertEqual(self.hash_table.get("key1"), "value1")
        self.assertEqual(self.hash_table.get("key2"), "value2")
        self.assertIsNone(self.hash_table.get("key3"))  

    def test_has(self):
        self.hash_table.set("key1", "value1")
        self.hash_table.set("key2", "value2")

        self.assertTrue(self.hash_table.has("key1"))
        self.assertTrue(self.hash_table.has("key2"))
        self.assertFalse(self.hash_table.has("key3"))  

    def test_repeated_word(self):
        sentence1 = "Once upon a time, there was a brave princess who..."
        sentence2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."
        sentence3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

        self.assertEqual(self.hash_table.repeated_word(sentence1), "a")  
        self.assertEqual(self.hash_table.repeated_word(sentence2), "it")  
        self.assertEqual(self.hash_table.repeated_word(sentence3), "summer")  



if __name__ == "__main__":
    unittest.main()
