"""this sorting maintains a sub array that is always sorted.

values from the unsorted part of the array are placed at the correct position in the sorted part.

it is  more efficient than other sorting algorithms, insertion sort has a time complexity of O(n^2) in the average and worst cases and O(n) in the best case"""

"""
Here we sort the following sequence using the insertion sort

Sequence: 7, 2, 1, 6


(7, 2, 1, 6) > (2, 7, 1, 6), In the first iteration, the first 2 elements are compared, here 2 is less than 7 so insert 2 before 7.


(2, 7, 1, 6) > (2, 1, 7, 6), In the second iteration the 2nd and 3rd elements are compared, here 1 is less than 7 so insert 1 before 7.


(2, 1, 7, 6) > (1, 2, 7, 6), After the second iteration (1, 7) elements are not in ascending order so first these two elements are arranged. So, insert 1 before 2. 


(1, 2, 7, 6) > (1, 2, 6, 7), During this iteration the last 2 elements are compared and swapped after all the previous elements are swapped. 
"""

def insertionsort(list1):

    #outer loop to transverse on len(list1)
    for i in range (1, len(list1)):
        a = list1[i]

        # move elements of list1[0 to i - 1] which are greater to one position ahead of their own current position
        j = i - 1

        while j>= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1

        list1[j + 1] = a

    return list1

list1 = [12, 11, 13, 5, 6]

print("Given array is:", list1)
print("Sorted array is:", insertionsort(list1))
        