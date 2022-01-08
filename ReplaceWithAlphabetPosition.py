def alphabet_position(text):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    final_str = str()
    for letter in text:
        letter = letter.lower()
        if letter in alphabet:
            final_str += f"{alphabet.index(letter)+1} "
    return final_str[:-1]


def main():
    x = input("What string do you want to test?")
    alphabet_position(x)


main()
