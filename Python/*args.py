#*args is used when we don't know  how  many positional parameters will ba passed.
#​*args​ ​collects extra positional arguments.​
# The collected values are stored as a tuple.​
# The name​ ​args​ ​is a convention; the​ ​*​ ​is important.
# Use​​*args​​when the number of arguments is flexible.​

def numbers(*numbers):
    print(numbers)

numbers(2,3,4,5)

def add_number(*number):
    total=0
    for i in number:
        total+=i
    return total
print(add_number(2,3,4))
