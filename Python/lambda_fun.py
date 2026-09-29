#Lambda function:are  small anonymous function.
#Anonymous function means do not need normal function name.
#syntax: lambda argument:expression

# ​Lambda functions are used for small one-line functions.​
# ​They can take any number of arguments.
# They can contain only one expression.​
# They automatically return the result of the expression.

def square(num):#normal function
    sq=num*num
    return sq
sq= square(4)
print(sq)


square= lambda num: (num*num)# lambda function
print(square(5))


#map function:map() ​​applies a function to every item of an iterable.​
#syntax:map(function,iterable)
num=[2,3,4,5]
sq=map(lambda num:num*num,num)
print(list(sq))


#filter()​​is used to select items from an iterable​ ​based on a condition.​
num=[1,2,3,4,5,6,7,8,9]
even_num=filter(lambda num: num %2==0,num)
print(list(even_num))