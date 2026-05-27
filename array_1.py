# import array as a
from array import *

arr_1 = array('i', [11, 12, 13, 14, 15,11,11])

#iterating over array elements directly
for eachElement in arr_1:
    print(eachElement)

#by using index
for i in range(len(arr_1)):
    print(arr_1[i])

print(arr_1[1 : 4].tolist())

cnt = arr_1.count(11)
print(cnt)

arr_1.append(142)
print(arr_1.tolist())

arr_1.insert(2,77)
print(arr_1.tolist())
arr_1.pop()
print(arr_1.tolist())

arr_1.reverse()

print(arr_1.tolist())
lst_1 = arr_1.tolist()
print(type(lst_1))