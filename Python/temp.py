#temperature converter
choice = input("Convert (C/F): ").upper()

temp = float(input("Enter temperature: "))

if choice == "C":
    fahrenheit = (9/5) * temp + 32
    print("Fahrenheit =", fahrenheit)

elif choice == "F":
    celsius = (5/9) * (temp - 32)
    print("Celsius =", celsius)

else:
    print("Invalid choice")