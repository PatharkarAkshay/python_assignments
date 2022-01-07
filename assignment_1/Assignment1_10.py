def CountCharCount(word):
    count = 0
    for x in word:
        count = count + 1

    return count


def main():
    print("Enter a string")
    name = input()
    ret = CountCharCount(name)
    print("Character count is ", ret)


if __name__ == "__main__":
    main()
