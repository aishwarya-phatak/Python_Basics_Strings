#strings
city = 'Pune is the Best!'
str_1 = 'Ganesh Festival'
str_2 = "I Love Pune"
print('Ganesh' in str_1)
print('Pune' in city, str_2)
print("Best" not in str_1)
print(str_1 + " " +city[5 :])
print(city[0 : 4] * 3)
name = "Bitcode Technologies"
length = len(name)

city_1 = 'Indore'
city_2 = "indore"
print(city_1 == city_2)

#
print(f"{name * 5}")   #multiplication operator with str
print("length of string : {}".format(length))
print(name[0])
print(name[0:3])

for i in range(0,length):
    print(name[i])