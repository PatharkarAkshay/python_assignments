def PrintStars(n):
  while n > 0:
    print("*", end="\t")
    n -= 1

def main():
  print("Enter number of stars -")
  n = int(input())
  PrintStars(n)

if __name__ == "__main__":
  main()

# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * *