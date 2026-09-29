#String is the combination of letters or words written inside single or double quotation.
print('Krishna')
print("Ram")


# Assigning variable to string
#- strings are assign to variable name by using equal(=).
a="Rakesh"
print(a)

b="""Multiline strings are 
assign to variable name by
 using three quotation"""
print(b)

a,b,c = 23,7,45 #multiple Variable assignment
print(a)
print(b)
print(c)

#same value to multiple variables
x=y=z=100
print(x)
print(y)
print(z)

#strings are Array:
#"""In Python, strings are sequence types,\n
#  not arrays. They behave like arrays in many ways because\n
#  they allow indexing, slicing, and iteration""".
text="Python"
print(text[0])#indexing
print(text[1:6:])#slicing
for i in text:
    print(i)


#strings are immutable.
#text[0]='r'
#print(text)

#string length
str="hare krishna hare krishna krishna krishna" \
"hare ram hare ram ram ram hare hare"
print(len(str))

#checking string
print("krishna" in str)

#check if not string
print("radhe"  not in str)