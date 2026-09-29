#Tuple:Tuple is immutable so we can not add or reove items from it.
#changing tuple into list to make change to it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 


#Add item in tuple
#Convert the tuple into a list, add "orange", and convert it back into a tuple:
fruits=('apple',"banana","papaya","cheery")
y= list(fruits)
y.append("orange")
fruits= tuple(y)
print(fruits)

#Create a new tuple with the value "orange", and add that tuple:
thistuple=("apple","mango","papya")
y=("orange",)
thistuple+=y
print(thistuple)

#Tuple packing:putting multiple values in single tuple.
fruits=("apple","banana","mango")
print(fruits)

#Tuple unpacking:the process of extracting the values of a tuple into separate variables.
fruits=("apple","banana","mango")
(green,red ,yellow)=fruits
print(green)
print(red)
print(yellow)


#Tuple unpacking means taking values from a tuple and putting them into variables.

#When we use *, it collects all the remaining values into a list.
fruits=("apple","mango","orange","papya","strawbeery")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#Loop in tuple
fruits=("apple","mango","orange","papya","strawbeery")
for i in fruits:
    print(i)


#Loop Through the Index Numbers
fruits=("apple","mango","orange","papya","strawbeery")
for i in range(len(fruits)):
    print(fruits[i])

#Join tuples
a=(2,3,5,6,7)
b=(9,34,23,98)
tuple= a + b
print(tuple)


#multiply tuples
fruits=("apple","mango","orange","papya","strawbeery")
tuple=fruits*2
print(tuple)