# R-1.1 Write a short Python function, is multiple (n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
def multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False
n = 10
m = 2
check = multiple(n, m)
print(f"{n} is a multiple of {m}: {check}

#R-1.2 Write a short Python function, is even (k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operator.

num = int(input("Enter a number: "))

def check(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
result = check(num)
print(result)

# R-1.3 Write a short Python function, minmax (data), that takes a sequence of three or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two, Do not use the built-in functions min or max in implementing your solution.
def minmx(Data):
    if len(Data) < 3:
        raise ValueError("Input sequence must contain at least three numbers")
    min_value, max_value = Data [0], Data [0]
    
    for number in Data[1:]:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    return min_value, max_value

Data = [1, 3, 8, 9, 0, 6, 76, 90, 567, 876, 2 , 3, 5]
result = minmx(Data)
print(result)

#R-1.4 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the even positive integers smaller than n.
num = int(input("Enter a number: "))
if num <= 0:
    raise ValueError("Invalid Number")

def sum_of_sqs(n):

    total = 0

    for i in range(2, n, 2):
        total += i ** 2
    return total
    
result = sum_of_sqs(num)
print(result)

#R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python's comprehension syntax and the built-in sum function.
result = sum(x ** 2 for x in range(2, num, 2))
print(result) 
        
