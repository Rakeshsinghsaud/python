#Comprehension is simple way to create new collection (list,set,dictionary) from existing collection.


num=[1,2,3,4,5]
square=[]
for i in num:
     square.append(i*i)
print(square)

#syntax: [expression for item in iterable if condition]

numbers=[1,2,3,4,5,6,7,8,9,10]#List comprehension
square=[i*i for i in numbers if i%2==0]
print(square)
