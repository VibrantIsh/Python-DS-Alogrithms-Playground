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

# Example usage:
u = Vec(3)
u.coords = [4, 2, 7]

v = Vec(3)
v.coords = [1, 3, 5]

d = u.m(v)
print(d)


