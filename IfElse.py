z = input("Enter your input: ")
if int(z) > 3:
    print(z, "is greater than 3",)
elif int(z) == 3:
    print(z, "is equal to 3")
else:
    print(z, "is Smaller than 3")
    

num = float(input("Enter a number: "))
print(num)
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")    
    
num = float(input("Enter a number: "))
print(num)
if num >= 0 or num == 0:
    print("Positive Number")
else:
    print("Negative number")

a = float(input("Enter a first number: "))
b = float(input("Enter a second number: "))
print(a)
print(b)

if a >= b and a == b:
    print("Positive Number")
else:
    print("Negative number") 