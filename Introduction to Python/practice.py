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



    

