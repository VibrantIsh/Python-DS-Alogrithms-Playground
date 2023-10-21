# P-1.24 Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.
counter = 0
num = int(input("Enter a number: "))
if num <= 2:
    print("Number must be greater than 2")
else:
    while num >= 2:
        num = num / 2
        counter += 1

    print(counter)
