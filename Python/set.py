#set
#syntax:{}
#Set is  unordered mutable collection of elements.
# key features:
      # -unordered
      # -not indexed
      # -doesnot allow duplicate element
      # - mutable
set={2,4,5,23,45}
for i in set:#accessing items
   print(i)

fruits={'apple','mango','orange'}
print("apple" in fruits)

fruits={'apple','mango','orange'}
fruits.add("cheery")#add item
print(fruits)

a={2,3,4,5}
b={8,9,23,45}
a.update(b)
print(a)

fruits={'apple','mango','orange'}
fruits.remove("apple")#remove item
print(fruits)

for i in fruits:#loop in set
   print(i)

#set operations
a={4,5,6,8,20}
b={6,7,9}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))