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

