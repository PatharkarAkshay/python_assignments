class BankAccount:
  ROI = 10.5
  
  def __init__(self, n, a):
    self.name = n
    self.amount = a

  def Deposit(self, n):
    self.amount = self.amount + n

  def Withdraw(self, n):
    self.amount = self.amount - n
  
  def CalculateInterest(self):
    n = self.amount * BankAccount.ROI / 100

    print("Interest calculate - ", n)
    print("Amount after interest", n + self.amount)

  def Display(self):
    print("Name ",self.name)
    print("Amount ",self.amount)

def main():
  obj = BankAccount("Akshay", 5000)
  print("Enter the amount you want to deposit -")
  n = float(input())
  obj.Deposit(n)

  print("Enter the amount you want to withdraw -")
  n = float(input())
  obj.Withdraw(n)

  obj.CalculateInterest()
  obj.Display()

if __name__ == "__main__":
  main()

# 2. Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.