# P-2.29 Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish. The ecosystem consists of a river, which is modeled as a relatively large list. Each ele- ment of the list should be a Bear object, a Fish object, or None. In each time step, based on a random process, each animal either attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish dies (i.e., it disappears).

import random

class A:
    def __repr__(self):
        return 'B'

class C:
    def __repr__(self):
        return 'F'

class D:
    def __init__(self, E, F, G):
        self.H = E
        self.I = [None] * E
        self.J(F, C, G)
        self.J(A, F, G)
        
    def J(self, K, L, M):
        for _ in range(L):
            N = random.randint(0, self.H - 1)
            while self.I[N] is not None:
                N = random.randint(0, self.H - 1)
            self.I[N] = K()
    
    def O(self):
        P = [None] * self.H
        for Q in range(self.H):
            if self.I[Q] is not None:
                R = random.choice([Q - 1, Q, Q + 1])
                if 0 <= R < self.H and P[R] is None:
                    P[R] = self.I[Q]
                else:
                    P[Q] = self.I[Q]
        self.I = P
    
    def S(self):
        for T in range(self.H):
            if isinstance(self.I[T], A):
                for U in range(max(0, T - 1), min(self.H, T + 2)):
                    if isinstance(self.I[U], A) and U != T:
                        if self.I[U] is None:
                            self.I[U] = A()
                        elif isinstance(self.I[U], A):
                            self.I[T] = None
            elif isinstance(self.I[T], C):
                for U in range(max(0, T - 1), min(self.H, T + 2)):
                    if isinstance(self.I[U], C) and U != T:
                        if self.I[U] is None:
                            self.I[U] = C()
                        elif isinstance(self.I[U], C):
                            self.I[T] = None
                    elif isinstance(self.I[U], A):
                        self.I[T] = None
    
    def V(self, W):
        for X in range(W):
            self.O()
            self.S()
            self.Y()

    def Y(self):
        print(''.join([str(Z) if Z is not None else '-' for Z in self.I]))

D = D(15, 5, 10)
D.V(10)

