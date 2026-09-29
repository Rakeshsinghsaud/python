#list
 #syntax:[]
 #- List is ordered and mutable collection of elements.
  #key features:
   #  - mutable
    # - ordered
     #- allow duplicate
     #- Heteregenous element 
     #- indexed
#Accessing list items
list=["apple","banana","orange","mango","kiwi","cherry","guava"]
print(list[0])
print(list[3])
print(list[-1])#negative indexing
print(list[2:5:])#range of indexes
print(list[-4:-1])#range of negative indexes

# check if item exist
if "guava" in list:
    print("yes ,apple is in fruit list")


    list[0]='dragone fruit'#changing item in list
    print(list)
    list[1:3]="grapes","papya"#changing range in list
    print(list)


    #insert item in list
    list1=["apple","banana","orange","mango","kiwi","cherry","guava"]
    list1.insert(0,'watermellon')
    print(list1)

    #append items:used to add item at the end.
    list1.append("pomogranate")
    print(list1)

    #extend:add the elements into the list.
    a=[2,3,5,6]
    b=[4,7,8,9]
    a.extend(b)
    print(a)
    b.extend(a)
    print(b)

    #remove items in list
    a1=[23,45,56,78]
    a1.remove(23)
    print(a1)

#Loop in list
l=[2,56,78,90,900]
for i in l:#loop through list
    print(i)

for i in range(len(l)):#loop through index number
    print(l[i])

    i=0
    while i<len(l):#while loop
        print(l[i])
        i+=1