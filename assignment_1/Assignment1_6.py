def CheckNumber(no):
    if no > 0:
        print("Positive number")
    elif no < 0:
        print("Negative number")
    else:
        print("Zero")


def main():
    print("Enter a number")
    number = int(input())
    CheckNumber(number)


if __name__ == "__main__":
    main()
