# worst case : O(n^2)
# average case : O(n^2)
# best case : O(n) -> array already sorted
# space complexity : O(1) constant since we don't require any extra space or data structures

def bubbleSort(array):

    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


array = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(array)
print(array)
