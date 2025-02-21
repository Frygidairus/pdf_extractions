from pypdf import PdfReader, PdfWriter

PATH_TO_PDF = "./etl_sample.pdf"

def normalize_pdf(input_pdf, output_pdf="normalized.pdf"):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    return output_pdf

normalized_pdf = normalize_pdf(PATH_TO_PDF)

reader = PdfReader(PATH_TO_PDF)
txt = ""

for page in reader.pages:
    print("PAGE NUMBER ",page.page_number)
    print(page.extract_text())
    txt+= page.extract_text()

with open("./extracted_pypdf_norm.txt", "w") as f:
    f.write(txt)