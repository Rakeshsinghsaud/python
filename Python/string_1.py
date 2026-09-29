#slicing
a="hello, world"
print(a[0:4])
print(a[:5:])#slice from start
print(a[2::])#slice from end
print(a[0])#indexing
print(a[-5:-2:])#negative indexing


#Modifying string
print(a.capitalize())
print(a.lower())
print(a.upper())

#strip() function is ued to remove whitespace from beginning and end of text.
b=" krishna , Radha"
print(b.strip())

#split() breaks a string into a list of parts based on whitespace (by default).
print(b.split())

#The replace() method replaces a string with another string:
print(b.replace("k","r"))

#string concatenation:add or combine two strings using + operator.
a="krishna"
b='ram'
print(a+b)
c = a + " " +b
print(c)



#f-string
name="krishna"
age=23
print(f"my name is {name} and age is {age}")

#placeholder:A placeholder is a symbol that represents where a value will be inserted.
name = "Krishna"

print("My name is %s" % name)

#Modifier:A modifier changes how the value is displayed, such as its width or number of decimal places.
price = 25.6789

print("%.2f" % price)