def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    first = 0
    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        # find middle using integer division
        middle = (first + last) // 2

        if arr[middle] == target:
            found = True
            return middle

        else:
            if target < arr[middle]:
                # search lower half of remainder
                last = middle - 1
            else:
                # search upper half of remainder
                first = middle + 1

    return -1  # not found
