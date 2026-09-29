# ​Function annotations are used to add type hints to function parameters and return values.
# syntax: def function_name(parameter: type) -> return_type:​
  #               ​statement​

# ​Function annotations describe expected data types. They make code easier to​ ​understand.​
# ​They help editors and tools detect possible mistakes.​
# ​Python does not automatically enforce these types at runtime.​

def add(a:int,b:int)->int:
    return a+b
print(add(3,23))

