# OOP: Object Oriented Programming
# class:blueprint(plan or way to create something).
# object:actual thing made from class.
# why OOP ?
# To organize large problem.
# To reuse the code.
# To model real world entities.
# To group data and behavior together.
""" syntax: class classname:#class 
              statement  """
""" syntax: object_name = classname()"""

# Attributes:Attributes are the value or property that belongs to class or object.

""" syntax:  object_name.attribute_name= value"""

#Example:
class student:
    name=""
    age=0

student1 = student()
student1.name="Krishna"
student1.age=23
print(student1.name)
print(student1.age)