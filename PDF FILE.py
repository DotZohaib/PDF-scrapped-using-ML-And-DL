import PyPDF2
a= PyPDF2.PdfFileReader('pdf.pdf')

# print(z.documentInfo)
# print(z.getNumPages())

str = ""
for i in range(1, 10):
    str += a.getPage(i).extractText()
    with open ("text.txt", "w", encoding= 'utf-8') as f:
        f.write(str)