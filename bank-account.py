from datetime import datetime
time =  datetime.now()
print(time)

class BankAccount:
  
  
  def __init__(self, first_name, last_name,bank):
    self.first_name=first_name
    self.last_name=last_name
    self.bank=bank
    self.balance=0
    self.phone_number=0
    self.deposits=[]
    self.withdrawals=[]
    self.loans=[]
    
  def account_name(self):
    name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
    return name
    
  def deposit(self, amount)
      self.balance += amount  
    try:
            amount + 1
        except TypeError:
             print("Enter amount in figures")
             return
           
      if amount>0
        print(" you have deposited{} to your account".format(amount)
       else:
         print("Low amount")
    
     
  def get_balance(self, amount):
      return "Balance for {} is {}".format(self.account_name(),self.balance)
      
    
  def withdraw(self, amount):
              try:
            amount + 1
        except TypeError:
             print("Enter amount in figures")
             return
              
    if amount <= 0:
        print("Amount cannot be withdrawn")

    elif amount > self.balance:
        print ("Insufficient Amount!!:", amount)
      
    else:
        self.balance -= amount
        print ("Withdrawal Successful:",amount)
        return
      
  def display(self):
    print ("Your Net Balance = {}".format(self.balance))   
    
  def withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            print(withdrawal)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))
            return
  
  def loan_given(self,amount):for deposit in self.deposits:
       print("You have received a loan of {}:".format(amount))
      self.loan= self.loan + amount
      
  def loan_repayed(self,amount):
      if amount >=1:
          self.repay=self.loan-amount
          print("You have repayed Ksh {}".format(amount))
          print("Your loan balance is: {}".format(self.repay)
                
  def loan_reduction(self,amount):
       if amount>=0:
           self.reduce=self.loan-amount
           print("loan reduced to Ksh{}.format(amount))
