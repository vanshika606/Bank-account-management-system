from bank import *

Dave=BankAccount(1000,"Dave")
Sara=BankAccount(2000,"Sara")

Dave.getBalance()
Sara.getBalance()

Sara.depos(500)

Dave.withdraw(100)
Dave.withdraw(10)

Dave.transfer(10000,Sara)
Dave.transfer(10,Sara)

Jim=InterestRewardAcct(1000,"Jim")
Jim.getBalance()
Jim.depos(100)
Jim.transfer(100,Dave)

Blaze=SavingAcct(1000,"Blaze")

Blaze.getBalance()

Blaze.depos(100)

Blaze.transfer(10000,Sara)
Blaze.transfer(1000,Sara)