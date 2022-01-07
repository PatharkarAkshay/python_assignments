def Addition(number1, number2):
    result = number1 + number2
    return result


def main():
    print("Enter two numbers")
    no1 = int(input())
    no2 = int(input())

    ret = Addition(no1, no2)
    print("Addition is ", ret)


if __name__ == "__main__":
    main()
