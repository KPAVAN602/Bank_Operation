class Bank:
    bankname = "Union Bank of India"
    adress = "CTR,AP,India"

    #create account
    def  __init__(self,user_name,pan,adress):
        self.user_name = user_name
        self.pan = pan
        self.adress = adress
        self.balance = 0.0
        print(f'Hello {self.user_name}, cong! your account created successfully')

    #deposit
    def deposit(self,amount):
        self.balance = self.balance+amount
        print(f'{amount} Deposited Successfully')

    #withdraw
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance = self.balance-amount
            print(f'{amount} Withdraw successfully')
        else:
            print("----Insufficient Fund ------")
    def ministatement(self,amount):
        print(f"Your Bank Balance is{self.balance}")


            
print(f'Welcome to {Bank.bankname},{Bank.adress}')
user_name = input("enter your name:")
pan = input("enter PAN number:")
adress = input("enter your adress:")

b = Bank(user_name,pan,adress) #object creation based on user provied data

while True:
    print("please select any option")
    print("1.Deposit\n2.Withdraw\n3.Ministatement\n4.Close")
    option = int(input())

    if option == 1:
        amount = float(input("Enter Deposited amount:"))
        b.deposit(amount)
        
    elif option == 2:
        amount = float(input("Enter withdraw amount:"))
        b.withdraw(amount)
        
    elif option == 3:
        b.ministatement(amount)
        
    elif option == 4:
         print("Thanks for choosing Union Bank of india")
         break