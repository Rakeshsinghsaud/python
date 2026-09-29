#Function:Functions are used to perform specific task.
#functions used to avoid repitation of same code again.
#Function run when it is called.
#Functions make code reuseable,clean and easy to understand.
#function types:
# 1. Built_in function: function defined by python itself.
#eg: print(),len()
#2.user_defined function:function defined by user.
#eg: def greet()
#syntax:
#   def function_name(paramter,paramter):
#
#   functio_name(argument,argument)

def greet(name):#parameter are variable written inside function definition and receive the value passed by fuction call.
    print("Hello",name)

greet("krishna")#argument are actual value written inside function call.
greet("Radhe")
greet("Ram")