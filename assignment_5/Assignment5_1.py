class Demo:
  value = 27
  def __init__(self, number1, number2):
    self.no1 = number1
    self.no2 = number2

  def fun(self):
    print("From fun")
    print(self.no1)
    print(self.no2)

  def gun(self):
    print("from gun")
    print(self.no1)
    print(self.no2)

def main():
  Obj1 = Demo(11, 21)
  Obj2 = Demo(51, 101)
  Obj1.fun()
  Obj2.fun()
  Obj1.gun()
  Obj2.gun()

if __name__ == "__main__":
  main()
    
# 1.Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance
# variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()