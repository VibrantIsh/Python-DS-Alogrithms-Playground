# R-2.5 If the parameter to the make_payment method of the Credit Card class were a neg ative number, that would have the effect of raising the balance on the account. Revise the implementation so that it raises a ValueError if a negative value is sent.
class CrdtCard:
    def __init__(self, num, blnc=0):
        self.num = num
        self.blnc = blnc

    def mk_paymnt(self, amnt):
        if amnt < 0:
            raise ValueError("Negative payment amount")
        self.blnc -= amnt
crd = CrdtCard("1234567890", 100)

try:
    crd.mk_paymnt(-50)
except ValueError as e:
    print(e)

print("Balance after invalid payment:", crd.blnc)

# R-2.6 The Credit Card class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a nonzero balance using an optional fifth parameter to the constructor. The four-parameter constructor syntax should continue to pro- duce an account with zero balance.
class CrdtCard:
    def __init__(self, num, hldr, exp_date, sec_code, blnc=0):
        self.num = num
        self.hldr = hldr
        self.exp_date = exp_date
        self.sec_code = sec_code
        self.blnc = blnc

crd_zero_blnc = CrdtCard("1234567890", "John Doe", "12/25", "1234")
print("Initial balance (Zero balance):", crd_zero_blnc.blnc)

crd_nonzero_blnc = CrdtCard("9876543210", "Jane Smith", "11/24", "5678", 500)
print("Initial balance (Nonzero balance):", crd_nonzero_blnc.blnc)

# R-2.7 Modify the declaration of the first for loop in the CreditCard tests, from Code Fragment 2.3, so that it will eventually cause exactly one of the three credit cards to go over its credit limit. Which credit card is it
class CrdtCard:
    def __init__(self, num, limit):
        self.num = num
        self.limit = limit
        self.blnc = 0

    def charge(self, amnt):
        if self.blnc + amnt > self.limit:
            print(f"Limit reached for card {self.num}")
        else:
            self.blnc += amnt

lim = 1000
crd = CrdtCard("1234", lim)
crd.charge(1200)

# R-2.8 Implement the sub method for the Vector class of Section 2.3.3, so that the expression u - v returns a new vector instance representing the difference between two vectors.
class Vec:
    def __init__(self, dim):
        self.dim = dim
        self.coords = [0] * dim

    def __repr__(self):
        return f"Vec({self.coords})"

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, idx):
        return self.coords[idx]

    def __setitem__(self, idx, val):
        self.coords[idx] = val

    def s(self, o):
        if len(self) != len(o):
            raise ValueError("Vectors must have the same dimension for subtraction")
        
        r = Vec(len(self))
        for i in range(len(self)):
            r[i] = self[i] - o[i]
        
        return r
u = Vec(3)
u[0] = 4
u[1] = 2
u[2] = 7

v = Vec(3)
v[0] = 1
v[1] = 3
v[2] = 5

d = u.s(v)
print(d)

# R-2.9 In Section 2.3.3, we note that our Vector class supports a syntax such as v=u+[ 5, 3 , 10, -2, 1], in which the sum of a vector and list returns a new vector. However, the syntax v=[ 5, 3 10, -2, 1] + u is illegal. Explain how the Vector class definition can be revised so that this syntax generates a new vector.
class Vec:
    def __init__(self, dim):
        self.dim = dim
        self.coords = [0] * dim

    def __repr__(self):
        return f"Vec({self.coords})"

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, idx):
        return self.coords[idx]

    def __setitem__(self, idx, val):
        self.coords[idx] = val

    def __add__(self, o):
        if len(self) != len(o):
            raise ValueError("Vectors must have the same dimension for addition")
        
        r = Vec(len(self))
        for i in range(len(self)):
            r[i] = self[i] + o[i]
        
        return r

    def __radd__(self, o):
        return self + o
u = Vec(5)
u[0] = 1
u[1] = 2
u[2] = 3
u[3] = 4
u[4] = 5

v = [5, 3, 10, -2, 1] + u
print(v)



# R-2.10 Implement the_mul method for the Vector class of Section 2.3.3, so that the expression v three returns a new vector with coordinates that are three times the respective coordinates of v. Also provide additional support for syntax 3v
class Vec:
    def __init__(self, dim):
        self.dim = dim
        self.coords = [0] * dim

    def __repr__(self):
        return f"Vec({self.coords})"

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, idx):
        return self.coords[idx]

    def __setitem__(self, idx, val):
        self.coords[idx] = val

    def __mul__(self, s):
        return Vec(len(self), [c * s for c in self.coords])

    def __rmul__(self, s):
        return self * s

v = Vec(4)
v[0] = 1
v[1] = 2
v[2] = 3
v[3] = 4

r1 = v * 3
print(r1)

r2 = 3 * v
print(r2)


# R-2.11 Implement the mul method for the Vector class of Section 2.3.3, so that sion uv returns a scalar that represents the dot product of the vectors, that is, sum i = 1 to d u i * v i .
class Vec:
    def __init__(self, dim):
        self.dim = dim
        self.coords = [0] * dim

    def __repr__(self):
        return f"Vec({self.coords})"

    def __getitem__(self, idx):
        return self.coords[idx]

    def m(self, o):
        return sum(a * b for a, b in zip(self.coords, o.coords))
u = Vec(3)
u.coords = [4, 2, 7]

v = Vec(3)
v.coords = [1, 3, 5]

d = u.m(v)
print(d)


# R-2.12 The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to 0. Another convenient form for creating a new vector would be to send the constructor a parameter that is some iterable type representing a sequence of numbers, and to create a vector with dimen sion equal to the length of that sequence and coordinates equal to the sequence val- ues. For example, Vector ([4, 7, 51) would produce a three-dimensional vector with coordinates < 4 7, 5. Modify the constructor so that either of these forms is accept- able; that is, if a single integer is sent, it produces a vector of that dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.
class Vec:
    def __init__(self, arg):
        try:
            self.c = list(arg)
            self.d = len(arg)
        except TypeError:
            self.d = arg
            self.c = [0] * arg

    def __repr__(self):
        return f"Vec({self.c})"

v1 = Vec(5)
print(v1)

v2 = Vec([4, 7, 5])
print(v2)

v3 = Vec((1, 2, 3, 4))
print(v3)

#  R-2.14 Implement a class inheritance program for the following set of classes:
#• Class Goat extends object and adds an instance variable_tail and methods milk () and jump (). • Class Pig extends object and adds an instance variable_nose and methods
#eat (food) and wallow (). • Class Horse extends object and adds instance variables_height and_color, and methods run () and jump ().

class G:
    def __init__(self, t):
        self.t = t

    def m(self):
        print("Goat is milking.")

    def j(self):
        print("Goat is jumping.")

class P:
    def __init__(self, n):
        self.n = n

    def e(self, f):
        print(f"Pig is eating {f}.")

    def w(self):
        print("Pig is wallowing.")

class H:
    def __init__(self, h, c):
        self.h = h
        self.c = c

    def r(self):
        print("Horse is running.")

    def j(self):
        print("Horse is jumping.")

g = G("short")
g.m()
g.j()

p = P("short")
p.e("vegetables")
p.w()

h = H("tall", "brown")
h.r()
h.j()


# R-2.15 Give a short fragment of Python code that uses the progression classes from Section 2.4.2 to find the 8th value of a Fibonacci progression that starts with 2 and 2 as its first two values.
class F:
    def __init__(self, f=0, s=1):
        self.f = f
        self.s = s

    def g(self, n):
        if n == 1:
            return self.f
        elif n == 2:
            return self.s
        else:
            p = self.f
            c = self.s
            for _ in range(2, n):
                p, c = c, p + c
            return c

fp = F(2, 2)
r = fp.g(8)
print(r)

# R-2.19 The collections. Sequence abstract base class does not provide support for compar- two sequences to each other. Modify our Sequence class from Code Fragment 2.14 to include a definition for the leg method, to support lexicographic comparison seql <= seq2.
from abc import ABC, abstractmethod

class seq(ABC):
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def __getitem__(self, j):
        pass
    
    def __le__(self, other):
        if len(self) != len(other):
            raise ValueError("sequences must have same length for comparison")
        
        for i in range(len(self)):
            if self[i] < other[i]:
                return True
            elif self[i] > other[i]:
                return False
        return True

class mySeq(seq):
    def __init__(self, elements):
        self._elements = list(elements)
    
    def __len__(self):
        return len(self._elements)
    
    def __getitem__(self, j):
        return self._elements[j]

seq1 = mySeq([1, 2, 3])
seq2 = mySeq([1, 2, 4])
seq3 = mySeq([1, 2, 3])

print(seq1 <= seq2)
print(seq1 <= seq3)
print(seq2 <= seq1)



