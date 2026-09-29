# Variable name should be short.
# Rules for variable name:
#-Variable name start with letter or underscore character.
#-Variable name can't start with digits or number.
#-Variable name contain  alpha-numberic and underscore character.
#-Variable name are case sensitive (age and Age are different)
#-Variable name cannot be python keywords.

var="Krishna"
var_23="krishna"
_var22='Krishna'
print(var)
#23var=45 ,variable cannot start with digits or number
#import='Raka',keyword cannot be variable name



#Assign multiple variables
x,y,z='apple','banana','orange'
print(x)
print(y)
print(z)

x=y=z='krishna'#assign one value to multiple variable
print(x)
print(y)
print(z)


#Global varible
s="Radha"
def greet():
    print("Godesses:",s)
greet()