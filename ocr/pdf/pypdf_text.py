from PyPDF2 import PdfFileReader

# open the PDF file
pdfFile = open("sampledoc.pdf", "rb")

# create PDFFileReader object to read the file
pdfReader = PdfFileReader(pdfFile)

print("PDF File name: " + str(pdfReader.getDocumentInfo().title))
print("PDF File created by: " + str(pdfReader.getDocumentInfo().creator))
print("- - - - - - - - - - - - - - - - - - - -")

numOfPages = pdfReader.getNumPages()

for i in range(0, numOfPages):
    print("Page Number: " + str(i))
    print("- - - - - - - - - - - - - - - - - - - -")
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
    print("- - - - - - - - - - - - - - - - - - - -")
# close the PDF file object
pdfFile.close()
