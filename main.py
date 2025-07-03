import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="📄",
    layout="wide"
)

# --- STYLING ---
st.markdown("""
    <style>
    /* Make sidebar wider */
    [data-testid="stSidebar"] {
        min-width: 300px;
        width: 300px;
    }

    /* Centered large title */
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

    /* Logo positioning */
    [data-testid="stSidebar"] img {
        display: block;
        margin: 1.5rem auto 2rem auto;
        width: 140px;
    }

    /* Radio buttons cleaned + custom selected + no blue bg */
    .stRadio div[role=radiogroup] label {
        background: #fff;
        padding: 0.6rem 1rem;
        border: 1px solid #ccc;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        transition: all 0.2s ease-in-out;
        color: #333;
        display: flex;
        align-items: center;
    }
    .stRadio div[role=radiogroup] label:hover {
        border-color: #007bff;
        background-color: #eef6ff;
        cursor: pointer;
    }
    .stRadio div[role=radiogroup] input:checked + div {
        background-color: #eef6ff !important;
        border: 1px solid #007bff !important;
        color: #007bff !important;
        font-weight: 600;
        box-shadow: 0 0 6px rgba(0, 123, 255, 0.3);
    }

    /* Change the radio dot to blue */
    .stRadio div[role=radiogroup] input[type="radio"] {
        accent-color: #007bff;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y")
    st.title("Navigation")
    choice = st.radio("Choose a tool", [
        "CVs & REFs Adapter",
        "Reference Creator",
        "CVs Extractor & Mapper"
    ])

# --- HEADER AREA ---
st.markdown("<div class='centered-title'>AO Tools Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart automation tools for project references & resumes</div>", unsafe_allow_html=True)
st.markdown("---")

# --- APP LOGIC ---
if choice == "CVs & REFs Adapter":
    st.subheader("CVs & REFs Adapter")
    st.write("Extract, align and enhance CVs & reference docs per AO instructions.")
    run_cvs_refs_adapter()

elif choice == "Reference Creator":
    st.subheader("Reference Creator")
    st.write("Generate complete bilingual references directly from reports.")
    run_ref_creator()

else:
    st.subheader("CVs Extractor & Mapper")
    st.write("Extract, map, and reformat CVs into your preferred structure.")
    run_cvs_adapter()
