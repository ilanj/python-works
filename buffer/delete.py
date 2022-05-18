text = "0123456789"

start = 2
end = 6

print(text[start : end])

text = text[0:start] + " " + text[start : end] + " " + text[end:]
print(text)
