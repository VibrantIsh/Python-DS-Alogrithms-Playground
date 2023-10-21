#P-1.26 Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons that are "pushed," and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process the basic arithmetic operations and a reset/clear operation.

# Simple calculator program
print(" Welcome to Pyhon Calculator")
screen = 0
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("6. Quit")
    
    try:
        choice = int(input("Enter your choice (1/2/3/4/5/6): ")
    except:
        print("Invalid input. Please choose a number from 1 to 6.")
        continue

    if choice == 1:
        try:
            num = int(input("Enter a number to add: "))
            screen = screen + num
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == 2:
        try:
            num = int(input("Enter a number to subtract: "))
            screen = screen - num
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == 3:
        try:
            num = int(input("Enter a number to multiply by: "))
            screen = screen * num
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == 4:
        try:
            num = int(input("Enter a number to divide by: "))
            if num == 0:
                print("Cannot divide by zero!")
            else:
                screen = screen / num
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == 5:
        screen = 0
        print("Screen cleared.")
    elif choice == 6:
        print("Thanks for using PyCalc 3000. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number from 1 to 6.")


