from pathlib import Path
import pdfplumber

def load_txt_md(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def load_pdf(path: Path) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def load_document(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in [".txt", ".md"]:
        return load_txt_md(path)
    elif suffix == ".pdf":
        return load_pdf(path)
    else:
        raise ValueError("Unsupported file type")
