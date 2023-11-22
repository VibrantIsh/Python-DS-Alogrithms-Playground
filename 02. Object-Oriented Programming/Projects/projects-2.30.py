# P-2.30 Suppose you are on the design team for a new e-book reader. What are the primary classes and methods that the Python software for your reader will need? You should include an inheritance diagram for this code. Your software architecture should at least include the func- tionality for customers to buy new books, view their list of purchased books, and read their purchased books. Write a r'ython program that simulates a system that supports the functions of an e-book reader. You should include methods to implement all the required functionalities for users of your system to "buy" new books, view their list of purchased books, and read their purchased books.
class Vyakti:
    def __init__(self, namak, likhak, content):
        self.shirshak = namak
        self.lekhak = likhak
        self.samagri = content

class Pustak:
    def __init__(self):
        self.pustak_soochi = []

    def pustak_kharid(self, pustak):
        self.pustak_soochi.append(pustak)

    def dekhe_kharidit_pustak(self):
        return [pustak.shirshak for pustak in self.pustak_soochi]

    def pustak_padhe(self, shirshak):
        for pustak in self.pustak_soochi:
            if pustak.shirshak == shirshak:
                return pustak.samagri
        return "Kharidit pustak soochi mein nahi mila"

n = Vyakti("Python Prakriya", "Rajiv Mishra", "Python Prakriya pustak ki samagri")
o = Vyakti("Data Structures", "Kamal Jain", "Data Structures pustak ki samagri")

p = Pustak()
p.pustak_kharid(n)
p.pustak_kharid(o)

q = p.dekhe_kharidit_pustak()
print("Kharidit pustak:", q)

r = p.pustak_padhe("Python Prakriya")
print("\nPustak padhna hai:", r)

