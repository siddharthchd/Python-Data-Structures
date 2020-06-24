def binary_search(array, beg, end, x):

    mid = (beg + end) // 2
    if array[mid] == x:
        return mid
    elif array[mid] > x:
        return binary_search(array, beg, mid-1, x)
    else:
        return binary_search(array, mid+1, end, x)
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, 0, len(test_list) - 1, test_val1))
print(binary_search(test_list, 0, len(test_list) - 1, test_val2))
