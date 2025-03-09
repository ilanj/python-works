from pdf2docx import Converter

pdf_file = "ila.pdf"
docx_file = "ila.docx"

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)  # all pages by default
cv.close()
