import streamlit as st
from pathlib import Path
import tempfile
from docx import Document
from .gpt_extract import extract_field
from .template_filler import fill_reference_table, fill_template_with_debug
from .utils import load_report_text
from deep_translator import GoogleTranslator

st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        max-width: 1000px;
        margin: auto;
    }

    /* TITLE */
    .ref-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 700;
        color: #1d3557;
        font-family: 'Segoe UI', sans-serif;
        margin-bottom: 0.5rem;
    }

    /* UPLOAD BOX */
    section[data-testid="stFileUploader"] {
        background: #f1f3f5;
        padding: 1.2rem 1rem;
        border: 1px solid #ced4da;
        border-radius: 10px;
        margin-bottom: 2rem;
    }

    /* BUTTON */
    button[kind="primary"] {
        background-color: #1d3557;
        color: #fff;
        padding: 0.6rem 1.2rem;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.2s ease;
    }

    button[kind="primary"]:hover {
        background-color: #2c5282;
        box-shadow: 0 0 6px rgba(29, 53, 87, 0.4);
        transform: scale(1.02);
    }

    /* DOWNLOAD BUTTON */
    .stDownloadButton > button {
        background-color: #339af0;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        margin-top: 1rem;
    }
    .stDownloadButton > button:hover {
        background-color: #1971c2;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='ref-title'>Reference Generator</div>", unsafe_allow_html=True)


def run_app():
    st.markdown("<div class='custom-title'>Reference Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='custom-desc'>Upload your project report and generate bilingual reference documents</div>", unsafe_allow_html=True)

    if "field_values" not in st.session_state:
        st.session_state["field_values"] = None
    if "output_path_fr" not in st.session_state:
        st.session_state["output_path_fr"] = None
    if "output_path_en" not in st.session_state:
        st.session_state["output_path_en"] = None

    uploaded_report = st.file_uploader(
        "Upload Project Report (.docx, .pdf, .pptx, .txt)", 
        type=["docx", "pdf", "pptx", "txt"]
    )
    submit = st.button("Submit", key="submit_ref_creator")

    # ✅ Reset the generation if a different file is uploaded
    if uploaded_report and "last_uploaded" in st.session_state:
        if uploaded_report.name != st.session_state["last_uploaded"]:
            st.session_state["generated"] = False

    # ✅ Update the uploaded filename in session
    st.session_state["last_uploaded"] = uploaded_report.name if uploaded_report else None

    TEMPLATE_PATH = "REF_creater/Référence Template.docx"

    def translate_docx(input_path, output_path, target_lang="en"):
        doc = Document(input_path)
        
        def translate_paragraph(para):
            text = para.text.strip()
            if text:
                try:
                    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
                    # Replace text of first run only
                    if para.runs:
                        para.runs[0].text = translated
                        for i in range(1, len(para.runs)):
                            para.runs[i].text = ""
                except Exception as e:
                    print("[Translation Error]", e)

        for para in doc.paragraphs:
            translate_paragraph(para)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        translate_paragraph(para)

        doc.save(output_path)

    # Process only once per upload
    if submit and uploaded_report:
        report_text = load_report_text(uploaded_report)

        with st.spinner("Extracting fields with GPT..."):
            st.session_state["field_values"] = fill_template_with_debug(TEMPLATE_PATH, report_text)

        with st.spinner("Generating French reference..."):
            filled_doc = fill_reference_table(TEMPLATE_PATH, st.session_state["field_values"])

            mission_name = st.session_state["field_values"].get("Nom de la mission", "output").strip()
            mission_name_safe = "".join(c for c in mission_name if c.isalnum() or c in (" ", "_", "-")).rstrip()

            # Save French version
            fr_name = f"{mission_name_safe}_ref_VF.docx"
            path_fr = Path(tempfile.gettempdir()) / fr_name
            filled_doc.save(path_fr)
            st.session_state["output_path_fr"] = path_fr

        with st.spinner("Translating to English..."):
            en_name = f"{mission_name_safe}_ref_VA.docx"
            path_en = Path(tempfile.gettempdir()) / en_name
            translate_docx(path_fr, path_en, target_lang="en")
            st.session_state["output_path_en"] = path_en

        st.session_state["generated"] = True

    # Download buttons
    if st.session_state["output_path_fr"]:
        with open(st.session_state["output_path_fr"], "rb") as f:
            st.download_button(
                label="📥 Download French Version",
                data=f,
                file_name=st.session_state["output_path_fr"].name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    if st.session_state["output_path_en"]:
        with open(st.session_state["output_path_en"], "rb") as f:
            st.download_button(
                label="📥 Download English Version",
                data=f,
                file_name=st.session_state["output_path_en"].name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
