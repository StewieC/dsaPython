"""this sorting technique repeatedly finds the minimum element and sorts it in order

during execution, for every iteratio, the minimum element of the unsorted sub array is arranged in the sorted subarray

selection sort is more efficient than bubble sort with a time complexity of O(n^2)"""

"""
Here we sort the following sequence using the selection sort

Sequence: 7, 2, 1, 6


(7, 2, 1, 6) > (1, 7, 2, 6), In the first traverse it finds the minimum element(i.e., 1) and it is placed at 1st position.


(1, 7, 2, 6) > (1, 2, 7, 6), In the second traverse it finds the 2nd minimum element(i.e., 2) and it is placed at 2nd position.


(1, 2, 7, 6) > (1, 2, 6, 7), In the third traverse it finds the next minimum element(i.e., 6) and it is placed at 3rd position.


After the above iterations, the final array is in sorted order, i.e., 1, 2, 6, 7.

"""

def selectionsort(arr, size):
    for s in range (size):
        min_idx = s

        for i in range (s + 1, size):
            #for sorting in descending order
            #for minimum element in each loop

            if arr[i] < arr[min_idx]:
                min_idx = i

        #arranging min at the correct position
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])

#driver code
data = [2,3,54,12,456,6,67,4,224,5,34]
size = len(data)
selectionsort(data, size)
print("sorted array is : ", data)