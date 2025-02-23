import math

def search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        if arr[pos] == target:
                return pos
        elif arr[pos] < target:
                low = pos + 1
        else:
                high = pos - 1
    return -1