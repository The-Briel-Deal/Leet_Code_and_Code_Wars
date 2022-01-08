def duplication_count(text):
    list = []
    text = text.lower()
    for x in range(len(text)):
        for y in range(len(text)):
            if x != y:
                print(f"{text[x]} {text[y]}")
                if text[x] == text[y] and not (text[x] in list):
                    list.append(text[x])
    return len(list)


def main():
    while True:
        x = input("What string do you want to test?")
        print(duplication_count(x))


main()
