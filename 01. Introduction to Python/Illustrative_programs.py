# E-1.1 Write a program to prompt a user to enter his/her name and mailing address and display the entered information on the screen.
name = input("Enter your name: ")
address = input("Enter your mailing address: ")

print("\nName: " + name)
print("Mailing Address: " + address)


# E-1.2 Write a program to compute the area of different shapes and display the information on the screen.
import math 

def rectangle_area(length, width):
    return length * width 

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, heigth):
    return 0.5 * base * heigth 

while True:
    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Quit")
    
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        radius = float(input("Type the radius of the Circle here: "))
        area = circle_area(radius)
        print (f"The area of the Circle is {area}")

    elif choice == 2:
        length = float(input("Type the length of the Rectangle here: "))
        width = float(input("Type the width of the Rectangle here: "))
        area = rectangle_area(length, width)
        print (f"The area of the Rectangle is {area}")

    elif choice == 3:
        base = float(input("Type the base of the Triangle here: "))
        heigth = float(input("Type the heigth of the Triangle here: "))
        area = triangle_area(base, heigth)
        print (f"The area of the Triangle is {area}")
    
    elif choice == 4:
        break
    
    else:
        print("Invalid Choice!")

print("Goodbyeee")


# E-1.3 Write a program to compute the factorial of a given number and display the result on the screen.

#Using Math Module
import math
fact = int(input("Enter number: "))
factorial = math.factorial(fact)
print (f"{fact} factorial is: {factorial}")

#Using for loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
result = factorial_loop(num)
print(f"The factorial of {num} is {result}")

#Recursive Style
def loop(num):
    if num == 0:
        return 1
    else:
        result = num * loop(num - 1)
        return result
    
num = int(input("Enter number: "))
factorial = loop(num)
print(f"The factorial for {num} is {factorial}")

# E-1.4 Write  a program to find the =avg of N natural numbers where the value of N is entered through keyboard.
def find_avg(n):
    total_sum = 0
    for num in range(1, n + 1):
        total_sum += num
    avg = total_sum / n
    return avg

average = find_avg(num)
print(f"The average for {num} natural numbers is {average}")

# E-1.5 Write a program to find the GCD of two numbers.
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd_recursive(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")

# using math module
import math 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd = math.gcd(num1, num2)
print(gcd)

# E-1.7 Write a program that returns the number of vowels in a text where the text is entered through keyboard.
text = input("Enter your text: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels in the text are:", count)

#E-1.8 Write a program that returns the Chinese zodiac sign of a person where year of birth is entered through keyboard.
def zodiac():
    if (year - 1900) % 12 == 0:
        return 'Rat'
    elif (year - 1900) % 12 == 1:
        return 'Ox'
    elif (year - 1900) % 12 == 2:
        return 'Tiger'
    elif (year - 1900) % 12 == 3:
        return 'Rabbit'
    elif (year - 1900) % 12 == 4:
        return 'Dragon'
    elif (year - 1900) % 12 == 5:
        return 'Snake'
    elif (year - 1900) % 12 == 6:
        return 'Horse'
    elif (year - 1900) % 12 == 7:
        return 'Goat'
    elif (year - 1900) % 12 == 8:
        return 'Monkey'
    elif (year - 1900) % 12 == 9:
        return 'Rooster'
    elif (year - 1900) % 12 == 10:
        return 'Dog'
    elif (year - 1900) % 12 == 10:
        return 'Pig'
while True:
    print("Enter your year of birth")
    print("For example : 2004")
    year = int(input("Enter here: "))
    print(f"You're born in {year}")
    print ("Your Chinese Zodiac animal is:",zodiac())
    decision = input("Do you want to continue (Yes/No): ").lower()
    if decision == 'no':
        break

print("GoodByeeeee")

# E-1.9 Write a program to find the number of words in the text entered by the user and then to sort the words.
text = input("Enter the text here: ")
words = text.split()
count = 0
for i in words:
    count += 1
print(f"The Total word cound is {count}")

words.sort()
print("The words in sorted order are: ")
for w in words:
    print(w)

#E-1.10 Write a program to find the sum of only integer numbers in a list. For noninteger numbers, an exception is caught.
number = input("Enter a list of number seperated by a apce: ")
number.split()
sum = 0
for n in number:
    try:
        intnum = int(n)
        sum = sum + intnum
    except ValueError:
        print("Enter could not be converted into integer. Not Valid")




