def EvenNumbers(n):
  for i in range(1, n * 2 + 1):
    if (i % 2 == 0):
      print(i, end="\t")

def main():
  print("Enter even number to print -")
  n = int(input())
  EvenNumbers(n)

if __name__ == "__main__":
  main()

# 9. Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20