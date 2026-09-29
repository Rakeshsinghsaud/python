#Nested function:function inside another function.

def outer_fun():
    print("outter")
    def inner_fun():
        print("inner")

    inner_fun()
outer_fun()