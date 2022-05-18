import re
text = 'Allowed Hello Hollow'
for m in re.finditer('ll', text):
         print('ll found', m.start(), m.end())

text = 'positive'

# advisable
if text == 'positive':
    print(True)

# not advisable
if text is 'positive':
    print(True)