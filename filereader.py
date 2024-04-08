import PyPDF2
# from google.colab import drive

pdf_file_path = '/content/pdf.pdf'

pdf_reader = PyPDF2.PdfReader(pdf_file_path)

text = ""

for i in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[i].extract_text()

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(text)