# Challenge Title

## **Code Challenge no.28: Object Sort**

### Approach & Efficiency

## Movies Sorted Methods

1. By year .. this method sorts movies by year in descending order. It takes a list of movie objects as input and returns an ordered list of objects based on the most recent years.

2. By title .. this method sorts movies by title while ignoring leading "A"s, "An"s, or "The"s. It takes a list of movie objects as input and returns an ordered list of objects based on alphabetical order, ignoring the specified prefixes.

The code also includes a sample list of movie objects movies_set, and an instance of the Movies class called my_sort is created. The two methods are invoked on my_sort to demonstrate their functionality. <br>

- The space complexity of both methods is O(1) since they do not use any additional data structures that grow with the input size. <br>

- The Time complexity :

1. The time complexity of `movies_sorted_by_year` method is O(n log n) due to the sorting operation using the sorted function. Here, 'n' represents the number of movie objects in the input list.
2. The time complexity of `movies_sorted_by_title` method is also O(n log n) due to the sorting operation using the sorted function.

### Solution

To run the code, you have to pass an array and a value to be inserted:

- Test code: `pytest tests/test_objects_sort.py`
