def insertsort(arr, value):
    arr.append(value)
    
    length = len(arr)
    
    # Iterate over each element starting from the second one
    for i in range(1, length):
        key = arr[i]  
        
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  
            j = j - 1
        
        arr[j + 1] = key  
    return arr

print(insertsort([20, 18, 12, 8, 5, -2], 3))
print(insertsort([1,-1, 2, -2 , 3, -3],0))


