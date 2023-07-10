import pytest
from insertionsort.insertionsort import insertsort
def test_Reverse_sorted():
    actual=insertsort([20,18,12,8,5,-2],3)
    expected= [-2, 3, 5, 8, 12, 18, 20]
    assert actual== expected

def test_Reverse_sorted():
    actual=insertsort([1,-1,2,-2,3,-3],0)
    expected= [-3, -2, -1, 0, 1, 2, 3]
    assert actual== expected   


