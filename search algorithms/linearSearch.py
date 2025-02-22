def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

"""the function search takes in an array and a target value 
and returns the index of the target value in the array. 
If the target value is not in the array, 
the function returns -1. 
The function iterates through the array using a for loop and checks if each element is equal to the target value. 
If it finds a match, it returns the index of the element. 
If it doesn't find a match, it returns -1."""

#declare the array list
arr = [1,3,4,5,66,77,23,67]

#declare the target number for search
target = 23

#linear search drive code
result = search(arr, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("result not found")