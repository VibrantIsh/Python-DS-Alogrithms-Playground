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
