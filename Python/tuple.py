#Tuple

#syntax:()

 #Tuple is ordered,immutable collection of element.
#key features:
    #- ordered
    #- immutable
    #- indexed
    #- allow duplicate
    #- heteregenous element
tuple=('Krishna',"Radha",'Ram','Vishnu','Gobindha',"Krishna")
print(tuple)
print(len(tuple))
print(type(tuple))
tuple1=()#create empty tuple.
print(tuple1)

print(tuple[1])#accsdding tuple items
print(tuple[-1])#negative indexing
print(tuple[1:4:])#range of indexes


# del keyword is used to delete tulple completely.
#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists 
