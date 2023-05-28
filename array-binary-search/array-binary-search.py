def binary_search(arr, key):
    low = 0
    high = len(arr)-1
    mid = int(high/2)
    while (key != arr[mid]):
        mid = int((high-low)/2) + low
        if (key in arr[mid:high+1]):
            low = mid+1
            high = high
        elif (key in arr[low:mid]):
            low = low
            high = mid-1
        else:
            mid = -1
            break
    print(mid)


binary_search([1, 2, 3, 5, 6, 7], 6)
