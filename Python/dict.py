#Dictionary
# syntax:{k:v}
 #- Dictionary is unordered ,mutable collection of element (key value pairs)
 #- key features:
 #  - mutable
 #- unodered
  # -  allow duplicate:for only value,key shouldn't be duplicate
   #- not indexed

dict={"name":"raka","course":"python","age":23}
print(dict)
print(dict['name'])#accessing items
print(dict.get('course'))
print(dict.keys())
print(dict.values())
print(dict.items())

dict={"name":"raka","course":"python","age":23,"year":2026}#changing items
dict['age']=24
print(dict)


dict={"name":"raka","course":"python","age":23,"year":2026}
dict.update({"year":2003})#update dictionary
print(dict)

dict={"name":"raka","course":"python","age":23,"year":2026}
dict['color']="green"#adding items
print(dict)

dict.pop('age')#removing items
print(dict)
dict.popitem()#remove last item
print(dict)


#loop

dict={"name":"raka","course":"python","age":23,"year":2026}
for i in dict:
    print(i)#keys

for i in dict:
    print(dict[i])#values

dict1={"name":"raka","course":"python","age":23,"year":2026}
for i in dict1.values():
    print(i)
for i in dict.keys():
    print(i)

x={"name":"raka","course":"python","age":23,"year":2026}   
y=x.copy()#copying dictionary
print(y)

z={"name":"raka","course":"python","age":23,"year":2026}
z.clear()#romoving dictioary
print(z)

#Nested dictioary
student={
    'student1':
    {"name":"Krishna","age":23},
    "student2":{
        'name':"Rake",'age':24
    }
    
}
print(student)