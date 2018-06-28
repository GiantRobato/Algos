# Prompt: Given an list of integers, sort them using selection sort
# 
# Example:  
# Input: [0, -3, 4, 16, 23, 18]
# Output: [-3, 0, 4, 16, 18, 23]
#
# Edge cases:
#   Blank Input
#     Input: []
#     Output: []
#
#   Single Input 
#     Input: [1]
#     Output: [1]


def selection_sort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        tmp = arr[i]                
        arr[i] = arr[minIdx]
        arr[minIdx] = tmp
    return arr

tests = []
tests.append([])
tests.append([1])
tests.append([1,2])
tests.append([2,1])
tests.append([1,2,3])
tests.append([3,2,1])
tests.append([0, -3, 4, 16, 23, 18])

for testNum in range(len(tests)):
    print("Test #{0}".format(testNum))
    print("Input:\t{0}".format(tests[testNum]))
    print("Output:\t{0}".format(selection_sort(tests[testNum])))