import unittest
from hashmapLeftJoin.hashmap_left_join import left_join


class TestLeftJoin(unittest.TestCase):
    def test_left_join_common_keys(self):
        dict1 = {'fond': 'enamored', 'wrath': 'anger', 'diligent': 'employed', 'outfit': 'garb', 'guide': 'usher'}
        dict2 = {'fond': 'averse', 'wrath': 'delight', 'diligent': 'idle', 'guide': 'follow', 'flow': 'jam'}

        result = left_join(dict1, dict2)

        expected = [['fond', 'enamored', 'averse'],
                    ['wrath', 'anger', 'delight'],
                    ['diligent', 'employed', 'idle'],
                    ['outfit', 'garb', None],
                    ['guide', 'usher', 'follow']]

        self.assertEqual(result, expected)

    def test_left_join_no_common_keys(self):
        dict1 = {'apple': 'red', 'banana': 'yellow'}
        dict2 = {'orange': 'orange', 'kiwi': 'green'}

        result = left_join(dict1, dict2)

        expected = [['apple', 'red', None],
                    ['banana', 'yellow', None]]

        self.assertEqual(result, expected)

    def test_left_join_partial_common_keys(self):
        dict1 = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
        dict2 = {'banana': 'yellow', 'orange': 'orange'}

        result = left_join(dict1, dict2)

        expected = [['apple', 'red', None],
                    ['banana', 'yellow', 'yellow'],
                    ['grape', 'purple', None]]

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()