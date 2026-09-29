#student Grade calculator
marks1=int(input("enter marks in maths"))
marks2=int(input("enter marks in science"))
marks3=int(input("enter marks in computer"))
marks4=int(input("enter marks in english"))
total_marks = marks1 + marks2 + marks3 + marks4
percent = total_marks/4
print("total_marks:",total_marks)
print("percentage:",percent)
if percent>=80:
    print("Grade is A")
elif percent>=60:
    print("Grade is B")
elif percent>=40:
    print("Grade is C")
else:
    print("failed")