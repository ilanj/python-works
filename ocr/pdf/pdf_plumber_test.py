import pdfplumber

with pdfplumber.open("sampledoc.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.chars[0])