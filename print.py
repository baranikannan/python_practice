print(5 + 10)
print("5 + 10")
print('5 + 10')
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  
print(37 / 3) 
print(37 // 3)  
print(37 % 3)  


print('What is your name?')
name = input()
print('Hi ' + name + '!')

name = input("What is your name? ")

test_text = input ("Enter a number: ")

test_number = int(test_text)

print(test_number)

test_number = int(input("Enter a number: "))

print(test_number)

print(int(input("Enter a number: ")))


test3word = input("Tell me your lucky number: ")

try:
    test3num = int(test3word)
    print("This is a valid number! Your lucky number is: ", test3num)
except ValueError:
    print("This is not a valid number. It isn't a number at all! This is a string, go and try again. Better luck next time!")
    
    
    