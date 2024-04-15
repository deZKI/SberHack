import PyPDF2
from io import BytesIO


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    pdf_file = BytesIO(pdf_bytes)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text() if page.extract_text() else ''
    return text
