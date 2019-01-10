import sys

class Customer:
    bankName='National Bank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Hello After Deposit Balance:',self.balance)

    def WithDraw(self,amount):
        if amount>self.balance:
            print('Sorry!...Insufficient Funds')
            sys.exit()
        else:
            self.balance=self.balance-amount
            print('Hello After WithDraw Balance:',self.balance)

print("Welcome to "+Customer.bankName)
name=input('Enter Your Name:')
c=Customer(name)
print("Hello",c.name,"Your accout got created")
while True:
    print('D-Deposit\nW-WithDraw\nE-Exit')
    option=input('Chosse Your Option:')
    if option =='D' or option =='d':
        amount=float(input('Enter amount:'))
        c.deposit(amount)
    elif option=='W' or option=='w':
        amount=float(input('Enter amount to WithDraw:'))
        c.WithDraw(amount)
    elif option=='E' or option=='e':
        print('Thanks for Banking')
        sys.exit()
    else:
        print('Invalid option!...Please Try Again')
