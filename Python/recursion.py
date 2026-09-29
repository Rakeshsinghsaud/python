# Recursiom means function call itself.
# syntax:
# def function_name():
#    function_name()

# ​Recursion is used when a problem can be broken into smaller versions of the same​ problem.
# ​A recursive function calls itself.
# ​Every recursion must have a base case.
# ​The base case stops the recursion.
# Without a base case, recursion continues until python rasies recursionError.

def factorial(num):
    if num==1:# this is base case
        return 1 #stop the recursion here
    return num *factorial(num -1)
print(factorial(5))
