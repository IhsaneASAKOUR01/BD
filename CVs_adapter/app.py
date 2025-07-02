import streamlit as st
from .resume_extractor import extract_all_parts_by_section_titles
from .section_mapper import semantic_map_sections, gpt_fill_template_as_text, gpt_fill_as_dict
from .resume_extractor import extract_full_text
from pathlib import Path
import tempfile
from .docx_generator import fill_docx_template_by_labels
import os

def run_app():
    st.title("📄 CV Section Extractor & Mapper")

    uploaded_resumes = st.file_uploader("Upload Resume(s) (.docx)", type=["docx"], accept_multiple_files=True)
    uploaded_template = st.file_uploader("Upload Template (.docx)", type=["docx"])
    submit = st.button("🚀 Submit", key="submit_cv_adapter")


    if submit and uploaded_resumes and uploaded_template:
        with st.spinner("Processing resumes..."):
            template_tmp = tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_template.name).suffix)
            template_tmp.write(uploaded_template.getbuffer())
            template_tmp.flush()
            template_path = template_tmp.name
            template_raw_text = extract_full_text(template_path)

            for uploaded_resume in uploaded_resumes:
                resume_tmp = tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_resume.name).suffix)
                resume_tmp.write(uploaded_resume.getbuffer())
                resume_tmp.flush()
                resume_path = resume_tmp.name

                output_name = f"UPDATED_{Path(uploaded_resume.name).stem}.docx"
                output_path = os.path.join(tempfile.gettempdir(), output_name)

                # Extract and process
                resume_text = extract_full_text(resume_path)
                filled_dict = gpt_fill_as_dict(template_raw_text, resume_text)
                fill_docx_template_by_labels(template_path, filled_dict, output_path)

                # Display debug
                with st.expander("📄 Resume Extracted Text"):
                    st.text(resume_text)
                with st.expander("🧾 Template Raw Text"):
                    st.text(template_raw_text)
                with st.expander("🤖 GPT Output (Dict)"):
                    st.json(filled_dict)

                # Download
                with open(output_path, "rb") as f:
                    st.download_button(
                        label=f"📥 Download {output_name}",
                        data=f,
                        file_name=output_name,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )