from numpy import *

#reshape
a = array([1,2,3,4,5,6])
b = a.reshape(2,3)
print(a)
print(b)

#flatten
c = array([[1,2,3],[10,11,12]])
print(c)
print(c.flatten())

#any, all
arr_1 = array([10,11,12,13,14], int)
arr_5 = arr_1.view()        #similar array objects but at different memory areas

print(arr_1.nbytes)             #int32 #int64 #int
print(arr_1.shape)          #shape
print(arr_1.size)
print(arr_1.ndim)
print(arr_1.dtype)

arr_2 = array([10,2,13,13,5])
arr_4 = arr_1           #array aliasing not copy

#where
print(where(arr_1 % 2 == 0,True,False))

print(logical_and(arr_1 >= 10,arr_1<=12))
print(logical_or(arr_2 >= 5,arr_2 < 12))

arr_3 = (arr_1 == arr_2)
print(arr_3)
print(any(arr_3))
print(all(arr_3))

result = add(arr_1,arr_2)
result_1 = arr_1 + arr_2
print(result)
print(type(result))
print(arr_1 + 6)