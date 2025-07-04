import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
    <style>
    /* Container width and spacing */
    html, body, .stApp {
        font-family: 'Poppins', sans-serif !important;
        font-size: 13px !important;
        zoom: 0.85 !important;
        background-color: #f0f4f8v;
    }
    .main .block-container {
        max-width: 900px;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: auto;
    }
    
    /* Sidebar size + border */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
        width: 300px;
        min-width: 300px;
        border-right: 2px solid #dee2e6;
    }
    
    /* Logo */
    [data-testid="stSidebar"] img {
        display: block;
        width: 180px;
        margin-left: 2rem;
        margin-right: auto;
        margin-top: 1rem;
        margin-bottom: 4rem;
    }
    
    /* Title */
    .centered-title {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        color: #1d3557;
        margin-bottom: 0.2rem;
        font-family: 'Comic Neue', cursive;
    }
    .subtitle {
        text-align: center;
        color: #6c757d;
        margin-bottom: 2rem;
        font-size: 1rem;
    }
    
    /* Radio buttons */
    .stRadio div[role=radiogroup] > label {
        background: #fff;
        padding: 0.5rem 1rem;
        border: 1px solid #ddd;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        transition: all 0.2s ease-in-out;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .stRadio div[role=radiogroup] > label:hover {
        background-color: #eaf4ff;
        border: 1px solid #339af0;
        cursor: pointer;
    }
    .stRadio input[type="radio"] + div svg {
        fill: #339af0 !important;
    }
    .stRadio div[role=radiogroup] > label:has(input[type="radio"]:checked) {
        background-color: #eaf4ff;
        border: 1px solid #339af0;
        box-shadow: 0 0 4px rgba(51, 154, 240, 0.5);
        font-weight: 600;
        color: #222;
    }
    </style>

""", unsafe_allow_html=True)

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
