def search(arr, target, low, high):
    if low  <= high:
        mid  = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(arr, target, mid + 1, high)
        else:
            return search(arr, target, low, mid - 1)
    else:
        return -1
    
#declare the array list
arr = [1,3,4,5,66,77,23,67]

#declare the target number for search
target = 3

#binary search drive code
result = search(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("result not found")