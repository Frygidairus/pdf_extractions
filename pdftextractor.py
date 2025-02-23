import pymupdf
import re

def extract_text(path_to_pdf: str) -> str:
    """
    Extracts and cleans text from a PDF file while preserving formatting and removing unwanted elements.

    This function reads a PDF file using PyMuPdf, extracts text while preserving whitespaces,
    and filters out page numbers and figure captions. It also ensures proper spacing around punctuation.

    Args:
        path_to_pdf (str): The file path to the PDF document.

    Returns:
        str: The cleaned text extracted from the PDF, with unnecessary elements removed.
    """

    pdf = pymupdf.open(path_to_pdf)
    extracted_text = []

    # Keep all the default flags for the text extraction except for the ligatures flag (ie. 'ff' 'ffi'... as one character)
    flags = pymupdf.TEXT_PRESERVE_WHITESPACE | pymupdf.TEXT_MEDIABOX_CLIP | pymupdf.TEXT_CID_FOR_UNKNOWN_UNICODE

    for page in pdf:

        text = page.get_text(flags=flags)  # Extract text as plain text with line breaks
        lines = text.split("\n")  # Split into lines for easier processing
        cleaned_lines = []

        # Filter out page numbers and captions
        for line in lines: # Strips lines to remove unwanted spaces before checks
            if not line.strip().isdigit() and not line.strip().startswith("Figure"):
                cleaned_lines.append(line)
        
        extracted_text.append(" ".join(cleaned_lines))  # Rejoin text from a page
        
    full_text = " ".join(extracted_text) # Rejoin text from all pages
    clean_text = re.sub(r"\s+(\. ?\. ?\.|[.,!?:;])", r"\1", full_text) # Handle spaces before ponctuation
    
    return clean_text  # Return full cleaned text

if __name__ == "__main__":

    text = extract_text("etl_sample.pdf")
    print(text)

    with open("./extraction_test.txt", "w") as file:
        file.write(text)
