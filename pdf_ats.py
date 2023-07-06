from PyPDF2 import PdfReader
pdf_path = '/home/sourojit/Downloads/Sourojit_Resume_01.pdf'
reader = PdfReader(pdf_path)
print(reader.pages[0].extract_text())