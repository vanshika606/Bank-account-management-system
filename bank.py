class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance=initialAmount
        self.name=acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}'  balance = ${self.balance}")

    def depos(self,amount):
        self.balance=self.balance+amount
        print("\nDeposit complete")
        self.getBalance()

    def viableTrnsaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self,amount):
        try:
            self.viableTrnsaction(amount)
            self.balance=self.balance-amount
            print("\nwithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.viableTrnsaction(amount)
            self.withdraw(amount)
            account.depos(amount)
            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardAcct(BankAccount):
    def depos(self, amount):
        self.balance=self.balance+(amount*1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee=5

    def withdraw(self, amount):
        try:
            self.viableTrnsaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interuppted: {error}")