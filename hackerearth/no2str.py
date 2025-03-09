import sys

no_to_text = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
}
vowels = ["a", "e", "i", "o", "u"]


def no2words(no):
    if no not in no_to_text:
        q = no // 10
        q = q * 10
        r = no % 10
        return no_to_text[q] + " " + no_to_text[r]
    else:
        return no_to_text[no]


def computing():
    nos = []
    nos_w = []
    vo_t = []
    n = int(input())
    nbs = input()
    nos = nbs.split()
    nos = list(map(int, nos))

    for each in nos:
        nos_w.append(no2words(each))

    for cs in nos_w:
        c = 0
        for ch in cs:
            if ch in vowels:
                c = c + 1
        vo_t.append(c)
    sumofvow = sum(vo_t)
    print(sumofvow)
    res = 0
    for i in range(len(nos)):
        for j in range(i + 1, len(vo_t)):
            if nos[i] + nos[j] == sumofvow:
                res = res + 1
    if res > 100:
        print("greater 100")
    else:
        print(no2words(res), sep=" ", end="\n", file=sys.stdout)


computing()
