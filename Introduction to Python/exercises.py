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

        
