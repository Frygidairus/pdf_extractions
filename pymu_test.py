import pymupdf  # PyMuPDF

def extract_clean_text(pdf_path):
    doc = pymupdf.open(pdf_path)
    extracted_text = []

    for page in doc:
        text = page.get_text("text")  # Extract text as plain text
        lines = text.split("\n")  # Split into lines

        # Filter out unwanted lines (heuristic: page numbers and captions)
        cleaned_lines = [
            line for line in lines 
            if not line.strip().isdigit() and "Figure" not in line
        ]
        
        extracted_text.append("\n".join(cleaned_lines))  # Rejoin cleaned text

    return "\n\n".join(extracted_text)  # Return full cleaned text

# Example usage
pdf_path = "etl_sample.pdf"  # Path to your PDF file
clean_text = extract_clean_text(pdf_path)
print(clean_text)
