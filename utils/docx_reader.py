
import docx2txt

def extract_text_from_docx(uploaded_file):
    text = docx2txt.process(uploaded_file)
    return text
