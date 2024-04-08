from pypdf2 import PdfReader

pdf_reader = PdfReader('pdf.pdf')

page_content ={}

for indx, pdf_page in enumerate(pdf_reader.pages):
    page_content[indx + 1] = pdf_page.extract_text()
    print(page_content)