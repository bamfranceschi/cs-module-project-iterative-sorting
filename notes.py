[1, 3, 6, 8, 9]


def find_value_binary(arr, value):
    first = 0
    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        # find middle using integer division
        middle = (first + last) // 2

        if arr[middle] == value:
            found = True

        else:
            if value < arr[middle]:
                # search lower half of remainder
                last = middle - 1
            else:
                # search upper half of remainder
                first = midde + 1

    return found

# insertion sorting

    # mark first element as sorted
    # for each unsorted element x
    # 'extract" the element X
    # for j = lastSortedIndex down to 0
    # if current element j > x
    # move sorted element to the right by 1
    # break lop and insert X here


def insertion_sort(input_list):
    # mark first item as sorted, separate first element?
    # (no code needed here, conceptual)
    # for every item starting at the second element
    for i in range(1, len(input_list - 1)):
        # put current item in temp variable
        current_item = input_list[i]
        # look left until we find were it belonds
        look_left_index = i - 1
        # if we are not at the beginning and current item is less than sorted and
        while look_left_index > 0 and current_item < input_list[look_left_index]:
            # to find where it belongs
            # compare current item to sorted item
            # if sorted item is bigger, shift sorted item right
            input_list[look_left_index + 1] = input_list[look_left_index]
            look_left_index -= 1
        # if current item is greater than sorted or we are at the beginning of sorted
            # insert item
        input_list[look_left_index] = current_item

    return input_list
