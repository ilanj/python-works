import re

name= "ergr%4445%^$$T%$GGtG"

text= re.sub(r'[a-z][0-9]','', name)
print(text)

