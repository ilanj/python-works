import itertools

shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for each in result:
    print(each)

print("-------------------------------------")

shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations_with_replacement(shapes, 2)
for each in result:
    print(each)

# text = "apple banana mango orange"
# words = text.split()
# result = itertools.combinations(words, 2)
# for each in result:
#     each = each[0] + each[1]
#     print(each)
def get_as_bigram(text):
    # text = "apple banana mango"
    words = text.split()
    if len(words) == 1:
        yield text
    for i in range(len(words)-1):
        print(" ".join(words[i:i+2]))
        yield " ".join(words[i:i+2])
temp_list = [
    "aaa bbb ccc ddd",
    "Discharge summary",
    "hello word u",
    "how are u python",
    "hellooooooo",
    "Date of Discharge to hfgfg h"
]
bigrams = list()
for each in temp_list:
    for entry in get_as_bigram(each):
        bigrams.append(entry)
print(bigrams)
