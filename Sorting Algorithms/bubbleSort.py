def bubblesort(arr):

    n = len(arr)

# for loop to transverse through all elements in the array
    for i in range(n):
        for j in range(0, n-i-1):

            #range of the array is from 0 to n-i-1
            #swap the elements if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#driver code
arr = [64, 34, 25, 12, 22, 11, 90]

bubblesort(arr)
print("Sorted array is:", arr)