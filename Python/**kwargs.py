# **kwargs​​ is used when we do not know how many keyword​ ​arguments will be passed.​
# ​**kwargs ​​collects extra keyword arguments.
# The collected values are stored as a dictionary.​
# ​Keys are argument names.​
# ​Values are argument values.


def student_info(**detail):
    for key,value in detail.items():
        print(key, value)
    
student_info(name="Krishna",age=23,course="python")
student_info(name="Ram",course="Datascience")