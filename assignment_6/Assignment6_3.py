class Number:
  def __init__(self, no):
    self.value = no

  def ChkPrime(self):
    if self.value > 1:
      for i in range(2, self.value):
        if(self.value % i == 0):
          return False
        else:
          return True
    else:
      return False
  
  def ChkPerfect(self):
    sum = self.SumFactors()
    if sum == self.value and self.value!=1 :
      return True
    else:
      return False
  
  def Factors(self):
    print("Factors of -",self.value)
    for i in range(1, self.value + 1):
      if self.value % i == 0:
        print(i)

  def SumFactors(self):
    sum = 0
    for i in range(1, self.value):
      if self.value % i == 0:
        sum = sum + i
    return sum

def main():
  print("Enter number - ")
  number = int(input())
  Obj = Number(number)
  Obj.SumFactors()
  Obj.Factors()
  if Obj.ChkPrime():
    print(number," is prime number")
  else:
    print(number," is not prime number")

  if Obj.ChkPerfect():
    print(number," is Perfect number")
  else:
    print(number," is not Perfect number")

if __name__ == "__main__":
  main()

# 3. Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
# Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.