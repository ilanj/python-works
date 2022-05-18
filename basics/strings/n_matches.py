import re
text = 'Allowed Hello Hollow'
for m in re.finditer('ll', text):
         print('ll found', m.start(), m.end())

text = 'positive'

<<<<<<< HEAD
# advisable
if text == 'positive':
    print(True)

# not advisable
if text is 'positive':
=======
if text == 'positive':
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
    print(True)