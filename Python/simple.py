# Simple calculator
a=float(input("enter first number"))
b=float(input("enter second number"))
print("choose operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice=int(input("enter a choice(1/2/3/4)"))
if choice==1:
    print("Result:",a+b)
elif choice==2:
    print("Result:",a-b)
elif choice==3:
    print("Result:",a*b)
elif choice==4:
    if b!=0:
        print("Result:",a/b)
    else:
        print("divisble by zero")
else:
    print("Invalid ")
