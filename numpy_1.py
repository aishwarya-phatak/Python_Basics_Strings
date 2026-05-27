import numpy as np

arr_1 = np.array([1,2,3,4,5], dtype=int)
print(arr_1)
print(arr_1 + 10)

print(type(arr_1))
arr_2 = np.insert(arr_1,2,45)
print(arr_2)

arr_3 = np.delete(arr_1,1)
print(arr_3)

arr_4 = np.append(arr_1,[33,44,55])
arr_5 = np.append(arr_1,47)
arr_6 = np.append(arr_1,arr_2)

print(arr_4)
print(arr_5)
print(arr_6)

arr_7 = np.array([1,2,3],int)
arr_8 = np.array([11,12,13],int)
print(arr_7 + arr_8)



