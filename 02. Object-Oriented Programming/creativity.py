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
