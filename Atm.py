class atm():
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    input("Enter your name: ")
    card_number=input("Enter your card number: ")
    pin_number=input("Enter your pin number: ")
    def cashWithDrawl(self):
        input("Enter the withdrawl amount: Rs. ")
        print("Money has been successfully withdrawled")
    
    def balanceEnquiry(self):
        print("Currently you have Rs. 50,00,000 ")
        print("You have enough balance")
    
    def cashDeposit(self):
        input("Enter the deposit amount: Rs. ")
        print("Your cash has been safely deposited")

RBI_bank = atm('4535826747', '3562')

print(RBI_bank.cashWithDrawl())
print(RBI_bank.balanceEnquiry())
print(RBI_bank.cashDeposit())