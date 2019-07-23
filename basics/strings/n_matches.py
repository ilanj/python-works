import re
text = 'Allowed Hello Hollow'
for m in re.finditer('ll', text):
         print('ll found', m.start(), m.end())