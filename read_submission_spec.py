from docx import Document

doc = Document("docs/submission_spec.docx")

for para in doc.paragraphs:
    print(para.text)