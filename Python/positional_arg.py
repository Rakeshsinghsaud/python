#positional arguments are matched based on their position.
# function_name(parmeter1,parameter2):
#​ 1.​Python passes arguments in the same order as parameters.​
# 2.The first argument goes to the first parameter.
# 3.The second argument goes to the second parameter.​
# 4.Order matters in positional arguments.

def student_info(name,age):
    print(f"name is {name} and age is {age}")

student_info("Krishna",24)
student_info("Ram",23)



#Return:send the value back where the function is called.
# syntax:
#      def function_name():
#          return
# ​A function can return one value or multiple values.​
# ​After ​​return​​, the function stops executing.​
# ​If there is no ​​return​​, Python returns​ ​None​​ automatically.​

def add(a,b):
    result= a+b
    return result #return pass value back to function call(add)


result=add(23,4)
print(result)


#without return:none is seen
def greet():
   print("Hello")

result=greet()
print(result)

#Return multiple values
def calculator(a,b):
    total= a+b
    diff= a-b
    return total,diff
sum_result,diff_result=calculator(2,4)
print(sum_result)
print(diff_result)
