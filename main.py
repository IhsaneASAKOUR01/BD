import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

# --- CONFIG ---
st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="📄",
    layout="wide"
)

# --- STYLING ---
st.markdown("""
    <style>
    /* Main layout and background */
    .block-container {
        padding: 2rem 4rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }

    /* Title centered */
    .centered-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        color: #1d3557;
        margin-bottom: 0.2rem;
        font-family: 'Segoe UI', sans-serif;
    }

    .subtitle {
        text-align: center;
        color: #6c757d;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }

    /* Sidebar logo */
    [data-testid="stSidebar"] img {
        display: block;
        margin: 1rem auto 2rem auto;
        width: 120px;
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }

    /* Styled radio buttons */
    .stRadio div[role=radiogroup] label {
        background: #ffffff;
        padding: 0.6rem 1rem;
        border: 1px solid #ccc;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        transition: all 0.2s ease-in-out;
    }

    .stRadio div[role=radiogroup] label:hover {
        border-color: #007bff;
        background-color: #eef6ff;
        cursor: pointer;
    }

    .stRadio div[role=radiogroup] input:checked + div {
        background-color: #007bff !important;
        color: white !important;
        font-weight: bold;
        box-shadow: 0 0 5px rgba(0,123,255,0.6);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR WITH LOGO ---
with st.sidebar:
    st.image("https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y")
    st.title("Navigation")
    tool = st.radio("Choose a tool", [
        "CVs & REFs Adapter",
        "Reference Creator",
        "CVs Extractor & Mapper"
    ])

# --- HEADER CENTERED ---
st.markdown("<div class='centered-title'>AO Tools Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart automation tools for project references & resumes</div>", unsafe_allow_html=True)
st.markdown("---")

# --- ROUTING ---
if tool == "CVs & REFs Adapter":
    st.subheader("CVs & REFs Adapter")
    st.write("Extract, align and enhance CVs & reference docs per AO instructions.")
    run_cvs_refs_adapter()

elif tool == "Reference Creator":
    st.subheader("Reference Creator")
    st.write("Generate complete bilingual references directly from reports.")
    run_ref_creator()

else:
    st.subheader("CVs Extractor & Mapper")
    st.write("Extract, map, and reformat CVs into your preferred structure.")
    run_cvs_adapter()
