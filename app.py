import streamlit as st
from utils.docx_reader import extract_text_from_docx
from utils.pdf_plumber import extract_text_from_pdf

st.title("TrackSide AI")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_resume:

    if uploaded_resume.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_resume)
    else:
        text = extract_text_from_docx(uploaded_resume)

    st.success("Resume processed successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        text,
        height=400
    )