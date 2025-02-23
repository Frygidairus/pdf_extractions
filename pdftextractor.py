import pymupdf
import re

def extract_text(path_to_pdf):

    pdf = pymupdf.open(path_to_pdf)
    extracted_text = []

    # keep all the default flags for the text extraction except for the ligatures flag (ie. 'ff' 'ffi'... as one character)
    flags = pymupdf.TEXT_PRESERVE_WHITESPACE | pymupdf.TEXT_MEDIABOX_CLIP | pymupdf.TEXT_CID_FOR_UNKNOWN_UNICODE

    for page in pdf:

        text = page.get_text(flags=flags)  # Extract text as plain text with line breaks
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

if __name__ == "__main__":

    text = extract_text("etl_sample.pdf")
    print(text)

    with open("./extraction_test.txt", "w") as file:
        file.write(text)
