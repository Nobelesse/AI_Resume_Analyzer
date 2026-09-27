from modules.pdf_parser import extract_text_from_pdf

pdf_path = input("C:\\Users\\adity\\OneDrive\\Desktop\\sample_resume")

text = extract_text_from_pdf(pdf_path)

print("\nPDF CONTENT:\n")
print(text[:2000])