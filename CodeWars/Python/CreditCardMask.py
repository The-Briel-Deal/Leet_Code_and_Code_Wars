# return masked string
def maskify(cc):
    return "yaya" * 6
    # cc_length = len(cc)
    # masked_cc = str()
    # for x in range(cc_length - 4):
    #     masked_cc += "#"
    # masked_cc += cc[-4:cc_length]
    # return masked_cc


def main():
    while True:
        cc = input("What do you want me to mask?")
        print(f"Original: {cc}\nMasked:   {maskify(cc)}")


main()
