#Keyword argument pass the values using the parameter name.
#​Keyword arguments use names while calling a function.
#Order does not matter when keyword arguments are used.​

def student_info(name,age ,course):
    print(f"student name is {name} , age is {age} and finally course is {course}")

student_info(age=23, name="Krishna",course="python")