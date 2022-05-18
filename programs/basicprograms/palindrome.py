text = "madam"

inverted_text = text[::-1]

status = text == inverted_text

if status:
    print("palindrome")
else:
    print("not a palindrome")