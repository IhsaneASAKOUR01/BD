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
        zoom: 0.9 !important;
        background-color: #f8f9fa !important;
    }
    .main .block-container {
        max-width: 900px !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        margin: auto !important;
    }
    
    /* Sidebar size + border */
    [data-testid="stSidebar"] {
        background-color: #f0f0ff !important;
        width: 300px !important;
        min-width: 300px !important;
        border-right: 2px solid #dee2e6 !important;
    }
    
    /* Logo */
    [data-testid="stSidebar"] img {
        display: block !important;
        width: 210px !important;
        margin-left: 2rem !important;
        margin-right: auto !important;
        margin-bottom: 4rem !important;
    }
    
    /* Title */
    .centered-title {
        text-align: center !important;
        font-size: 4rem !important;
        font-weight: 800 !important;
        color: #1d3557 !important;
        margin-bottom: 0.2rem !important;
        font-family: 'Comic Neue', cursive !important;
    }
    .subtitle {
        text-align: center !important;
        color: #6c757d !important;
        margin-bottom: 2rem !important;
        font-size: 1.5rem !important;
    }
    
    /* Radio buttons */
    .stRadio div[role=radiogroup] > label {
        background: #fff !important;
        padding: 0.5rem 1rem !important;
        border: 1px solid #ddd !important;
        border-radius: 10px !important;
        margin-bottom: 0.5rem !important;
        transition: all 0.2s ease-in-out !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
    }
    .stRadio div[role=radiogroup] > label:hover {
        background-color: #eaf4ff !important;
        border: 1px solid #339af0 !important;
        cursor: pointer !important;
    }
    .stRadio input[type="radio"] + div svg {
        fill: #339af0 !important;
    }
    .stRadio div[role=radiogroup] > label:has(input[type="radio"]:checked) {
        background-color: #eaf4ff !important;
        border: 1px solid #339af0 !important;
        box-shadow: 0 0 4px rgba(51, 154, 240, 0.5) !important;
        font-weight: 600 !important;
        color: #222 !important;
    /* Label above radio (e.g., "Choose a tool") */
    .stRadio > label {
        font-size: 2rem !important;
        margin-bottom: 1rem !important;
    }
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
#st.markdown("---")

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
