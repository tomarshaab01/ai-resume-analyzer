"""Extract plain text from PDF, DOCX, or image resumes."""
import io
import os


def extract_text(filepath: str) -> str:
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.pdf':
        return _from_pdf(filepath)
    elif ext == '.docx':
        return _from_docx(filepath)
    elif ext in ('.png', '.jpg', '.jpeg'):
        return _from_image(filepath)
    return ''


def _from_pdf(path: str) -> str:
    try:
        import PyPDF2
        text = []
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text.append(page.extract_text() or '')
        return '\n'.join(text)
    except Exception as e:
        return f'[PDF extraction error: {e}]'


def _from_docx(path: str) -> str:
    try:
        from docx import Document
        doc  = Document(path)
        return '\n'.join(p.text for p in doc.paragraphs)
    except Exception as e:
        return f'[DOCX extraction error: {e}]'


def _from_image(path: str) -> str:
    """Basic image-to-text using Pillow (no OCR dep required)."""
    return '[Image uploaded — Gemini Vision will read this directly]'
