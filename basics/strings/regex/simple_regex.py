import re

document  = " bbbb born this is a sample text b birthday sd f b bday b-fgg Bgds B,hg bb b b b b b b bbbbbbb"

document = re.sub(r'^b\s+', '', document)
print(document)