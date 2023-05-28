def insertShiftArray(arr, val):

    mid = len(arr) // 2
    return arr[:mid] + [val] + arr[mid:]
arr = [42,8,15,23,42]
val = 16
new_arr = insertShiftArray(arr, val)
print(new_arr)
