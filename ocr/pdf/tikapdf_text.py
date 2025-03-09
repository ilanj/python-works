from tika import parser  # pip install tika

raw = parser.from_file("sampledoc.pdf")
print(raw["content"])
