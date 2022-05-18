'''
{"abc", "abcd", "ab", "abx"}; Write a program to find Longest Common Prefix
Output - “ab"
'''

input = ["abc", "abcd", "ab", "abx"]
iterations = len(input)
inp_length = [len(word) for word in input]
max_length = max(inp_length)
index_longest_word = inp_length.index(4)
longest_word = input[index_longest_word]
output = list()

for itr, ch in enumerate(longest_word):
    flag = 0
    for word in input:
        try:
            if ch == word[itr]:
                flag += 1
        except Exception as e:
            break
    if flag == 4:
        output.append(ch)
    else:
        break

print("".join(output))

input = ["abc", "abcd", "ab", "abx"]

output = ""

while(True):
    itr = 0
    for word in input:
        temp = input[itr]
        if temp == input[itr]:
            pass
        else:
            break
        output = output+temp
        itr += 1

print(output)




