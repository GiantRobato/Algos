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


def merge_sort_driver(arr):
    merge_sort(arr,0, len(arr))
    return arr

def merge(arr,l,m,r):
    L = arr[l:m]
    R = arr[m:r]
    i = 0
    j = 0
    k = l
    for x in range(k,r):
        if j >= len(R) or i < len(L) and L[i] < R[j]:
            arr[x] = L[i]
            i += 1
        else:
            arr[x] = R[j]
            j += 1

def merge_sort(arr, l, r):
    if r - l > 1:
        m = (l + r ) //2
        merge_sort(arr,l,m)
        merge_sort(arr,m,r)
        merge(arr,l,m,r)
    return

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
    print("Output:\t{0}".format(merge_sort_driver(tests[testNum])))