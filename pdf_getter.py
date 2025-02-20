from pypdf import PdfReader
import pdfplumber

PATH_TO_PDF = "./etl_sample.pdf"

reader = PdfReader(PATH_TO_PDF)
txt = ""

for page in reader.pages:
    print("PAGE NUMBER ",page.page_number)
    print(page.extract_text())
    txt+= page.extract_text()

with open("./extracted_pypdf.txt", "w") as f:
    f.write(txt)

txt = ""
with pdfplumber.open(PATH_TO_PDF) as pdf:
    for page in pdf.pages:
        print("PAGE NUMBER ",page.page_number)
        print(page.extract_text())
        txt+= page.extract_text()

with open("./extracted_pdfplumber.txt", "w") as f:
    f.write(txt)
