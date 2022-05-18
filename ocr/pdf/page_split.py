from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("/home/ila/Documents/personal/certificates/247_ai_certificates/paperwork/10_12.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)