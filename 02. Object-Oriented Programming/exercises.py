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

