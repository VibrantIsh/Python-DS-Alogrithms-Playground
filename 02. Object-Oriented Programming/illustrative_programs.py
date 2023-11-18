# E-2.1 A class Customer contains the following details: customer name, customer ID, customer account number. Write a program that initializes the data members and displays them.

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
