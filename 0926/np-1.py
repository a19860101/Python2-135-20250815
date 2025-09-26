import numpy as np

arr = np.array(123)
arr1 = np.array([1,2,3])
arr2 = np.array([
    [1,2,3],[4,5,6]
])
arr3 = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ],[
        [7, 8, 9],[10, 11, 12]
    ]
])

print(arr1[0])
print(arr2[0])
print(arr2[0,0])
print(arr2[1,-1])
print(arr3[0,1,0])
print(arr3[:1])


# print(arr)
# print(arr1)
# print(arr2)
# print(arr3)
#
# print(arr.ndim)
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)
