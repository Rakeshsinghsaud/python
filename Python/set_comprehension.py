# Creates a set (unique, unordered values).
# Syntax: {expression for item in iterable if condition}

num={i*i for i in range(10)} #set comprehension
print(num)

# Dictionary comprehension
# Creates a dictionary (key-value pairs).
# Syntax: {key: value for item in iterable if condition}
square={i:i*i for i in range(10)if i%3==0}
print(square)


# Generator Comprehension
# Creates a generator (lazy, memory-efficient, produces values on demand).
# Syntax: (expression for item in iterable if condition)
gen=(i*i for i in range(10))
print(gen)
print(list(gen))