import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="📄",
    layout="wide"
)

def load_css(path: str):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")  # Or "assets/style.css" if stored there

# === SIDEBAR ===
with st.sidebar:
    st.image("logo.png")
    choice = st.radio("Choose a tool", [
        "CVs & REFs Adapter",
        "REF Creator",
        "CVs Template Adapter"
    ])

# === HEADER ===
st.markdown("<div class='centered-title'>BD Tools Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart automation tools for project references & resumes</div>", unsafe_allow_html=True)
st.markdown("---")

# === MAIN ===
if choice == "CVs & REFs Adapter":
    st.subheader("CVs & REFs Adapter")
    st.write("Extract, align and enhance CVs & reference docs per AO instructions.")
    run_cvs_refs_adapter()

elif choice == "REF Creator":
    st.subheader("REF Creator")
    st.write("Generate complete bilingual references directly from reports.")
    run_ref_creator()

else:
    st.subheader("CVs Template Adapter")
    st.write("Extract, map, and reformat CVs into your preferred structure.")
    run_cvs_adapter()

