"""
string reverse and palindrome
"""

org="abbad"
rev="".join(reversed(org))
print(rev)

if org==rev:
    print("palindrome")
else:
    print("not a palindrome")

str1="India"
str2="abc"
str1=str1.join(str2)
print(str1)


"""
string reverse alternative

Assuming a is a string. The Slice notation in python has the syntax -
list[<start>:<stop>:<step>]
So, when you do a[::-1], it starts from the end towards the first taking each element. So it reverses a. 
This is applicable for lists/tuples as well.
"""
name = "onetwothree"
print(name[::-1])
