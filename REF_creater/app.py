import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from pathlib import Path
import tempfile
from docx import Document
from .gpt_extract import extract_field
from .template_filler import fill_reference_table, fill_template_with_debug
from .utils import load_report_text
from deep_translator import GoogleTranslator
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container

def load_css():
    css_path = Path(__file__).resolve().parent.parent / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




def run_app():
    load_css()

    # Init session state
    if "field_values" not in st.session_state:
        st.session_state["field_values"] = None
    if "output_path_fr" not in st.session_state:
        st.session_state["output_path_fr"] = None
    if "output_path_en" not in st.session_state:
        st.session_state["output_path_en"] = None

    st.markdown("""
    <style>
    .custom-dropzone {
        border: 2px dashed #5e60ce;
        background-color: #ffffff;
        border-radius: 16px;
        padding: 3rem;
        text-align: center;
        max-width: 600px;
        margin: 3rem auto 1rem auto;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        transition: 0.3s ease all;
        font-size: 1.2rem;
        font-weight: 600;
        color: #5e60ce;
        cursor: pointer;
    }
    .custom-dropzone:hover {
        background-color: #f0f0ff;
        box-shadow: 0 0 12px rgba(94, 96, 206, 0.3);
    }
    .hidden-upload {
        display: none;
    }
    .big-button .stButton>button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 12px;
        background: linear-gradient(135deg, #5e60ce, #7400b8);
        color: white;
        border: none;
    }
    .big-button .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 10px rgba(116, 0, 184, 0.3);
    }
    </style>
    
    <div class="custom-dropzone" onclick="document.getElementById('upload_real').click()">
        📄 Click to upload your project report
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_report = st.file_uploader(
        label="",
        type=["docx", "pdf", "pptx", "txt"],
        label_visibility="collapsed",
        key="upload_real"
    )
    
    if uploaded_report:
        st.success(f"✅ `{uploaded_report.name}` uploaded!", icon="📎")
    
    with st.container():
        with st.container():
            st.markdown('<div class="big-button">', unsafe_allow_html=True)
            submit = st.button("🚀 Generate Reference")
            st.markdown('</div>', unsafe_allow_html=True)







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


