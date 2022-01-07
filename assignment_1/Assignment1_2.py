def ChkNum(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def main():
    print("Enter a number")
    no = int(input())

    ChkNum(no)


if __name__ == "__main__":
    main()
