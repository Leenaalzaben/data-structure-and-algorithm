def reverse_array(*arrays):
    reversed_arrays = []
    for arr in arrays:
        reversed_arr = []
        for i in range(len(arr) - 1, -1, -1):
            reversed_arr.append(arr[i])
        reversed_arrays.append(reversed_arr)
    return reversed_arrays


arr1 = [1, 2, 3, 4, 5]
arr2 = [89, 2354, 3546, 23, 10, -923, 823, -12]
arr3 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 
        89, 97, 101, 103, 107, 109, 113, 127, 131, 
        137, 139, 149, 151, 157, 163, 167, 173, 179,
          181, 191, 193, 197, 199]
reversed_arrays = reverse_array(arr1, arr2, arr3)
print(reversed_arrays)
