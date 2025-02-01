def vincentBinarySearch(arr, target, low, high):
    while(high >= low):
        mid = int((high - low)/2) + low
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


myArr = [1,3,4,7,8,10,12,14,23,24,32,44]
target1 = 32
print(vincentBinarySearch(myArr, target1, 0, len(myArr)-1))

def vincentRecursiveBinarySearch(arr, target, low, high):
    if high >= low:
        mid = int((high - low)/2) + low
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            return vincentRecursiveBinarySearch(arr, target, mid + 1, high)
        else:
            return vincentRecursiveBinarySearch(arr, target, low, mid - 1)
    else:
        return -1

print(vincentRecursiveBinarySearch(myArr, target1, 0, len(myArr)-1))


################################################################################
'''
# Looped Binary Search in python
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

####################################################################################

# Recursive Binary Search in python
def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if x == array[mid]:
            return mid

        # Search the right half
        elif x > array[mid]:
            return binarySearch(array, x, mid + 1, high)

        # Search the left half
        else:
            return binarySearch(array, x, low, mid - 1)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
'''