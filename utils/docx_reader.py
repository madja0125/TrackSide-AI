import docx2txt

def extract_text_from_docx(uploaded_file):
    text = ""

    with docx.open(uploaded_file) as docx:
        for page in docx.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text