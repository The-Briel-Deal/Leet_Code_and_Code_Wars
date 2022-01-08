def is_isogram(string):
    string = string.lower()
    for x in range(len(string)):
        for y in range(len(string)):
            if x != y and string[x] == string[y]:
                return False
    return True


def main():
    x = input("What string do you want to test?")
    is_isogram(x)


main()
