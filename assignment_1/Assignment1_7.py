def CheckDivisibility(no):
    print(no % 5 == 0)


def main():
    print("Enter a number")
    number = int(input())
    CheckDivisibility(number)


if __name__ == "__main__":
    main()
