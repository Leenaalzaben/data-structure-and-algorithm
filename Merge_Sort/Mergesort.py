def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [8, 4, 23, 42]
arr1 = [-3,3,1,-1,2,-2]
arr2 = [1,17,1,17,1,17]
merge_sort(arr)
merge_sort(arr1)
merge_sort(arr2)

print(arr,arr1,arr2)