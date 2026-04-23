import pypdf
import sys

def extract(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        # Get first 10 pages to avoid too much output
        for i in range(min(10, len(reader.pages))):
            text += reader.pages[i].extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error: {e}"

files = [
    "/Users/paul/Prog 2 Godot/book-files/Cognitive_science_approaches_in_the_classroom_-_A_review_of_the_evidence.pdf",
    "/Users/paul/Prog 2 Godot/book-files/Great Teaching Toolkit Evidence Review.pdf"
]

for f in files:
    print(f"--- START {f} ---")
    print(extract(f))
    print(f"--- END {f} ---")
