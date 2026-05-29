from random import random

from numpy import *

# multidimensional array
arr = array([[10, 10], [12, 12]], int)
print(shape(arr))

arr_1 = array([[10], [12]], int)
print(shape(arr_1))

arr_2 = array([10, 11, 12, 13, 14], int)
print(shape(arr_2))

arr_3 = array([1], int)
print(shape(arr_3))

arr_4 = array([[11, 12, 13, 45,55], [12, 13, 14, 60,90]], int)
print(shape(arr_4))

print(arr_4[0: 1, 1: 4])        #slicing multip dimensional arrays

print(arr_4)
# arr_new = reshape(arr_4, (3, 2))
# print(arr_new)

for i in arr_4:
    for j in i:
        print(j, end=" ")
    print("\n")

arr_ones = ones((2, 2), int)
print(arr_ones)

arr_zeros = zeros((3, 3), int)
print(arr_zeros)

# eye
arr_eye = eye(3, 3, dtype=int)
print(arr_eye)

x = random.random()
print(x)

arr_x = random.rand(3)
arr_y = random.rand(3, 3)
print(arr_x)
print(arr_y)
