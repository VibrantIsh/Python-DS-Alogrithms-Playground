

#E-2.1 A class Customer contains the following details: customer name, customer ID, customer account number. Write a program that initializes the data members and displays them.
class Customer:
    def __init__(self, name, iden, acno):
        self.custname = name 
        self.identity = iden
        self.accnumber = acno
    def displat(self):
        print("Customer name: ", self.custname)
        print("Customer Identity", self.identity)
        print("Account Numner", self.accnumber)
name = input ("Enter name: ")
iden = input("Identity number: ")
acno = input ("Enter Account Number: ")
obj = Customer(name, iden , acno)
obj.displat()


# E-2.2 Write a Python class to represent a bank account. The class contains name of the account holder, account number, type of account, and balance amount as the data members. The member functions are as follows: to initialize the data members, to deposit an amount, to withdraw amount after checking balance, and to display name and balance.
class Customer:
    def __init__(self, name, iden, acno):
        self.custname = name 
        self.identity = iden
        self.accnumber = acno
    def displat(self):
        print("Customer name: ", self.custname)
        print("Customer Identity", self.identity)
        print("Account Numner", self.accnumber)
        
class Account(Customer):
    def __init__(self, custname, identity, accnumber, typeacc, bankbalance):
        super().__init__(custname, identity, accnumber)
        self.typeacc = typeacc
        self.bankbalance = bankbalance
    def deposit(self):
        amount = int(input("Enter the amount to depost: "))
        self.bankbalance = amount + self.bankbalance
    def withdraw(self):
        while 1:
            amount = int(input("Enter the amount to withdraw: "))
            if self.balance >= amount: 
                self.balance = amount - self.balance
                break
            else:
                print("Insufficient Balance")
    def print_balance(slef):
        super().displat()
name = input ("Enter name: ")
iden = input("Identity number: ")
acno = input ("Enter Account Number: ")
typeacc = input("Enter the account type[Saving/Current]: ")
balance = int(input("Enter the initial balance: "))
acc  = Account(name, iden, acno, typeacc, balance)
while 1:
    print("Enter 1 for deposit: ")
    print("Enter 2 for withdraw: ")
    print("Enter 3 for display balance: ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc.deposit()
    elif choice == 2:
        acc.withdraw()
    elif choice == 3:
        acc.print_balance()
    else:
        break



#E-2.3 Write a Python class that is initialized with a date and displays the date if the date entered is valid
import datetime
class Date:
    def __init__(self, dd, mm, yr):
        self.dd = dd
        self.mm = mm
        self.yr = yr
        self.__checkDate()
    def __checkDate(self):
        isValid = True
        try:
            datetime.datetime(self.yr, self.mm, self.dd)
        except ValueError:
            isValid = False
        if isValid:
            print("Input Date is Valid: ", self.dd, ".", self.mm, ".", self.yr)
        else:print("Date is Invalid")
try:
    date = input("Enter the date, month, year in the following format[dd.mm.yyyy]: ")
    dd = int(date.split("."[0]))
    mm = int(date.split("."[1]))
    yr = int(date.split("."[2]))        
except ValueError:
    print("Date entered is in incorrect format", date)
d = Date(dd, mm, yy   )    



#E-2.4 Write a Python class that finds the age of a person.
from datetime import date

class age:
    def __init__(self):
        pass
    
    def cAge(self, bD):
        td = date.today()
        try:
            b = bD.replace(year=td.year)
        except ValueError:
            b = bD.replace(year=td.year, month=bD.month + 1, day=1)

        if b > td:
            return td.year - bD.year - 1
        else:
            return td.year - bD.year
a = age()
print(a.cAge(date(1980, 3, 19)), 'years')


# E-2.5 Write an abstract class Animal with an abstract method makesSound. The abstract class is inherited by classes representing different animals and defines the abstract method to display the kind of sound those animals produce.


from abc import ABC, abstractmethod
class Animal (ABC):
    def makesound(self):
        pass
class Apes(Animal):
    def makesound(self):
        print("Apes Gibber......")
        
class Snake(Animal):
    def makesound(self):
        print("Snake hiss......")
class Dog(Animal):
    def makesound(self):
        print("Dog bark.......")
class Tiger(Animal):
    def makesound(self):
        print("Tiger roar......")
class Bear(Animal):
    def makesound(self):
        print("Bear Growl......")
ape = Apes()
ape.makesound()
snakes = Snake()
snakes.makesound()
dogs = Dog()
dogs.makesound()
tigers = Tiger()
tigers.makesound()
bears = Bear()
bears.makesound()

