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

#R-1.6 Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length 1, and expression s [k] is used for index -n < k <0, what is the equivalent index j≥ 0 such that s [1] references the same element?
# Define a string with length 1

s = "T"
j = 0
element_j = s[j]
print(f"s[0] = {element_j}")

k = -1
element_k = s[k]
print(f"s[-1] = {element_k}")

# R-1.7 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0,-2,-4,-6, -8? how to use Python's list comprehension syntax to produce the list
list_formation = [i for i in range(8, -10, -2)]
print (list_formation)

# R-1.8 Demonstrate  how to use Python's list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
mylist = [2 ** i for i in range(9)]
print(mylist)

#R-1.9 Python's random module includes a function choice (data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that returns a random choice from the given range. Using only the randrange function, implement your own version of the choice function.
import random
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choice = random.randrange(len(my_list))
print(choice)
