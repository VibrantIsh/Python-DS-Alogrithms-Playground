# C-2.20 The Sequence Iterator class of Section 2.3.4 provides what is known as a forward iter. ator. Implement a class named Reversed sequence Iterator that serves as a reverse iterator for any Python sequence type. The first call to next should return the last element of the sequence, the second call to next should return the second-to-last element, and so forth.
class RevSeqIter:
    def __init__(self, s):
        self.s = s
        self.i = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            e = self.s[self.i]
            self.i -= 1
            return e
        else:
            raise StopIteration()

seq = [1, 2, 3, 4, 5]
ri = RevSeqIter(seq)

for i in ri:
    print(i)



# C-2.21 In Section 2.3.5, we note that our version of the Range class has implicit support for iter- ation, due to its explicit support of both len and getitem. The class also receives implicit support of the Boolean test, "k in r" for Range r. This test is evaluated based on a forward iteration through the range, as evidenced by the relative quickness of the test 2 in Range (10000000) versus 9999999 in Range (10000000). Provide a more efficient implementation of the contains method to determine whether a particular value lies within a given range. The running time of your method should be independent of the length of the range
class R:
    def __init__(self, s, st=None, sp=1):
        if st is None:
            s, st = 0, s
        self.l = max(0, (st - s + sp - 1) // sp)
        self.s = s
        self.sp = sp

    def __len__(self):
        return self.l

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if 0 <= k < len(self):
            return self.s + k * self.sp
        else:
            raise IndexError('Index out of range')

    def c(self, val):
        if self.sp == 0:
            return val == self.s

        if self.sp > 0:
            return self.s <= val < self.s + self.l * self.sp
        else:
            return self.s >= val > self.s + self.l * self.sp

r = R(0, 10000000)
print(2 in r)
print(9999999 in r)

# C-2.22 The PredatoryCreditCard class of Section 2.4.1 provides a process_month method that models the completion of a monthly cycle. Modify the class so that once a customer has made ten calls to charge in the current month, each additional call to that function results in an additional $1 surcharge.
class PCC(CreditCard):
    def __init__(self, c, b, a, l, r):
        super().__init__(c, b, a, l)
        self.r = r
        self.m = 0

    def charge(self, p):
        s = super().charge(p)
        if s:
            self.m += 1
            if self.m > 10:
                self._balance += 1
        return s

    def process_month(self):
        self.m = 0
        super().process_month()

pcc = PCC("John Doe", "Bank X", "1234 5678 9101 1121", 1000, 0.05)

for _ in range(12):
    pcc.charge(100)

print(pcc.get_balance())
pcc.process_month()
print(pcc.get_balance())


# C-2.24 At the close of Section 2.4.1, we suggest a model in which the Credit Card class supports a nonpublic method,_set_balance (b), that could be used by subclasses to affect a change to the balance, without directly accessing the_balance data member. Implement such a model, revising both the Creditcard and PredatoryCreditCard classes accordingly.
class CC:
    def __init__(self, c, b, a, l):
        self.c = c
        self.b = b
        self.a = a
        self.l = l
        self._b = 0

    def ch(self, p):
        if p + self._b > self.l:
            return False
        else:
            self._b += p
            return True

    def mk_pmt(self, a):
        self._b -= a

    def g_b(self):
        return self._b

    def _s_b(self, new_b):
        self._b = new_b


class PCC(CC):
    def __init__(self, c, b, a, l, apr):
        super().__init__(c, b, a, l)
        self.apr = apr

    def p_m(self):
        if self._b > 0:
            mf = pow(1 + self.apr, 1 / 12)
            self._s_b(self._b * mf)


pcc = PCC("Ramesh Kumar", "Bank X", "1234 5678 9101 1121", 1000, 0.05)
pcc.ch(500)
print(pcc.g_b())
pcc.p_m()
print(pcc.g_b())


# C-2.25 Write a Python class that extends the Progression class so that each value in the pro- gression is the absolute value of the difference between the previous two values. You should include a constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults.
class P:
    def __init__(self, f=0):
        self.c = f

    def a(self):
        self.c += 1

    def __next__(self):
        if self.c is None:
            raise StopIteration()
        else:
            val = self.c
            self.a()
            return val

    def __iter__(self):
        return self

class ADP(P):
    def __init__(self, f=2, s=200):
        super().__init__(f)
        self.p = s

    def a(self):
        self.p, self.c = self.c, abs(self.c - self.p)

ad_prog = ADP()
result = [next(ad_prog) for _ in range(10)]
print(result)
