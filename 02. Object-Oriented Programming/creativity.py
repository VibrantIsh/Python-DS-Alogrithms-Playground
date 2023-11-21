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

