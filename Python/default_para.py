#Default parameter make the arguments optional
# If argument is provided then python use the given value.
# If argument is not provided then python use default value.

def greet(name="Krishna"):
    print(f" Hello , {name}")

greet("Ram")
greet()#default parameter is krishna
    