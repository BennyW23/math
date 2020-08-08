#!/usr/bin/env python3
def letterSum(string):
    total = -96 * len(string)
    for let in string.lower():
        total += ord(let)
    return total


def mean(string):
    total = 0
    for let in string.lower():
        total += ord(let)
    mean = total / len(string)
    return chr(int(mean))


def mode(string):
    string = string.lower()
    letters = sorted(string)
    modeLetter = letters[0]
    modeCount = 1
    curLetter = letters[0]
    count = 1
    index = 1
    while index < len(string):

        if letters[index] == curLetter:
            count += 1
        else:
            curLetter = letters[index]
            count = 1
        if count > modeCount:
            modeCount = count
            modeLetter = curLetter
        index += 1

    return modeLetter


def median(string):
    letters = sorted(string.lower())
    if len(string) % 2 == 1:
        return letters[int(len(string) / 2)]
    else:
        total = ord(letters[int(len(string) / 2) - 1]) + ord(
            letters[int(len(string) / 2)]
        )
        return chr(int(total / 2))


def test():
    words = ["test", "attitude"]
    for word in words:
        calculate(word)


def main():
    print("Please enter a string, or q! to exit")
    word = input().strip().lower()
    while word != "q!":
        calculate(word)
        print("Please enter a string, or q! to exit")
        word = input().strip().lower()


def calculate(word):
    print("The string is: {}".format(word))
    print(letterSum(word))
    print(mean(word))
    print(mode(word))
    print(median(word))
    print


if __name__ == "__main__":
    # test()
    main()
