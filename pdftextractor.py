import pymupdf
import re

class PdfTextractor:

    def __init__(self, path_to_pdf):
        self.pdf = pymupdf.open(path_to_pdf)

    def extract_text(self):

        extracted_text = []
        pdf = self.pdf 

        for page in pdf:

            text = page.get_text("text")  # Extract text as plain text with line breaks
            lines = text.split("\n")  # Split into lines for easier processing
            cleaned_lines = []

            #Filter out page numbers and captions
            for line in lines: #strips lines to remove unwanted spaces before checks
                if not line.strip().isdigit() and not line.strip().startswith("Figure"):
                    cleaned_lines.append(line)
            
            extracted_text.append(" ".join(cleaned_lines))  #Rejoin text from a page
            
        full_text = " ".join(extracted_text) #Rejoin text from all pages
        clean_text = re.sub(r"\s+(\. ?\. ?\.|[.,!?:;])", r"\1", full_text) #Handle spaces before ponctuation
        
        return clean_text  # Return full cleaned text

pdf = PdfTextractor("etl_sample.pdf")

text = pdf.extract_text()
print(text)
