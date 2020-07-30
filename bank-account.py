 from datetime import datetime
time =  datetime.now()
print(time)

class BankAccount:
  
  
  def __init__( first_name, last_name,bank):
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
  
  def request_loan(self,amount):
    try:
      amount+10:
      except TypeError:
        print("please request the amount in figures"):
        return
      if amount >=0:
        print("you cannot request a loan of thaat amount")
    else:
      self.loan= self.loan + amount
     print("You have received a loan of {}:".format(amount))
     
      
  def repay_loan(self,amount):
    try:
      amount+10:
      except TypeError:
        print("please repay the amount in figures")
        return
        
        if amount >=1:
          print("you cannot reapy that amount")
        elif self.loan==0;
        print("you dont have a loan at the moment")
        elif amount>self.loan:
          print("your loan is{},please enter amount that is less or equal".format(self,loan))
          else:
            self.loan-=bank account:
            

      def loan _repayment_statement(self):
        for repayment in self.loan_ repayments:
          time =repayment['time']:
          amount=repayment['amount']:
          formatted time =time.get_formatted _time(time)
          statement=("you repaid{} on {}".format(time))
          print(statement)

Class BankAccount (Account):
   def_init_(self,first_name,last_name,phone_number,bank):
        self.bank=bank
        super()._init_(first_name,last_name,phone_number)

Class MobileMoneyAccount(Account):
   def_init_(self,first_name,last_name,phone_number,service_provider):
      self.service_provider=service_provider
      self.airtime=[]
      super()._init_(first_name,last_name,phone_number)

      def buy_airtime(self,amount): 
             try:
               amount +1
            except TypeError:
              print("Enter the amount in figures")
              return

              if amount >self.balance
              print("you dont have enough balance your balance is{}".format(self. balance))
          else:
            self.balance-=amount
            time=datetime.now()
            airtime{
              "time":time
              "airtime":amount
              }
              self.airtime.append(airtime)
      def pay_bill(self,amount):
        try:
          except TypeError:
            print("Enter amount in figures")
            return
           if amount>self.balance
           print("you dont have enough amount your balance is{}".format(self.balance))
         else:
           self.balance-=amount
           time=datetime.now()
           pay_bill{
             "time":time
             "pay_bill":amount
           }
           self.pay_bill.append(pay_bill)

      def send_money(self,amount):
        try:
          except TypeError:
            print("Enter amount in figures")
            return
            if amount>self.balance
            print("you cannot that amount of money your balance is{}".format(self.balance))
          else:
            self.balance-=amount
            time=datetime.now()
            send-money{
              "time":time
              "send_money":amount
            }
            self.send_money.append(send_money)


          def receive_money(self,amount) :
            try:
            except TypeError:
              print("Enter amount in figures")
              print("you have received {} ,your new balance is{}".format(self.balance))
               self.receive_money.append(received_money)
              
          
