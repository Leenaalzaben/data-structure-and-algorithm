import pytest
from Merge_Sort.Mergesort import merge_sort

def test_marge_sort():

    arr = [8, 4, 23, 42]
    merge_sort(arr)
    assert arr == [4,8,23,42]

    arr = [-3,3,1,-1,2,-2]
    merge_sort(arr)
    assert arr == [-3, -2, -1, 1, 2, 3]

    arr = [1,17,1,17,1,17]
    merge_sort(arr)
    assert arr == [1, 1, 1, 17, 17, 17]