
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
import streamlit.components.v1 as components
import base64

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

    with st.container():
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    
        uploaded_report = st.file_uploader(
            "📄 Upload your project report",
            type=["docx", "pdf", "pptx", "txt"]
        )
    
        submit = st.button("Submit")
    
        if st.session_state.get("output_path_fr"):
            with open(st.session_state["output_path_fr"], "rb") as f:
                st.download_button("📥 Download French Version", f, file_name=st.session_state["output_path_fr"].name, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    
        if st.session_state.get("output_path_en"):
            with open(st.session_state["output_path_en"], "rb") as f:
                st.download_button("📥 Download English Version", f, file_name=st.session_state["output_path_en"].name, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    
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
