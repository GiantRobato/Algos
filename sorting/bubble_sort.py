# Prompt: Given an list of integers, sort them using bubble sort
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

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0,len(arr) - i - 1):
            if arr[j] > arr[j+1]:          
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

tests = []
tests.append([])
tests.append([1])
tests.append([1,2])
tests.append([2,1])
tests.append([1,2,3])
tests.append([3,2,1])

print("testing:")
for testNum in range(len(tests)):    
    print("test #{0}".format(testNum))
    print("input:\t{0}".format(tests[testNum]))
    print("output:\t{0}".format(bubble_sort(tests[testNum][:])))