def pig_it(string):
    string = string.split()
    print(string)
    int = 0
    for item in string:
        if item != "!" and item != "?":
            first_letter = item[0]
            list_string = list(item)
            print(list_string)
            del list_string[0]
            list_string.append(first_letter)
            item = "".join(list_string)
            string[int] = item + "ay"
        int += 1
    string = " ".join(string)
    return string


def main():
    x = input("What string do you want to test?")
    print(pig_it(x))


main()
