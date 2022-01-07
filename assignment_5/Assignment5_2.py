class Circle:
  PI = 3.14

  def __init__(self):
    self.radius = 0.0
    self.area = 0.0
    self.circumference = 0.0

  def accept(self):
    print("Enter value of radius")
    self.radius = float(input())

  def calculateArea(self):
    self.area = Circle.PI * self.radius * self.radius

  def calculateCircumference(self):
    self.circumference = 2 * Circle.PI * self.radius

  def display(self):
    print("Radius of Circle - ", self.radius)
    print("Area of Circle - ", self.area)
    print("Circumference of Circle - ", self.circumference)

def main():
  obj = Circle()
  obj.accept()
  obj.calculateArea()
  obj.calculateCircumference()
  obj.display()

if __name__ == "__main__":
  main()

# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance
# variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area,
# Circumference.
# After designing the above class call all instance methods by creating multiple objects.