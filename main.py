import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

# --- CONFIG ---
st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y",
    layout="wide"
)

# --- STYLING ---
st.markdown("""
    <style>
    body {
        background-color: #f7f9fb;
    }
    .block-container {
        padding: 2rem 4rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    .css-1v3fvcr {
        background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
        background-size: cover;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .stRadio > div {
        gap: 1rem;
    }
    .stRadio div[role=radiogroup] label {
        background: #ffffff;
        padding: 0.5rem 1rem;
        border: 1px solid #d3d3d3;
        border-radius: 8px;
        transition: 0.2s ease-in-out;
    }
    .stRadio div[role=radiogroup] label:hover {
        border: 1px solid #007bff;
        background-color: #f1f9ff;
    }
    .stRadio div[role=radiogroup] input:checked + div {
        color: #ffffff !important;
        background-color: #007bff !important;
    }
    h1, h2, h3 {
        font-family: 'Segoe UI', sans-serif;
        color: #1c1c1c;
    }
    .app-logo {
        width: 140px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("Navigation")
tool = st.sidebar.radio("Choose a tool", [
    "CVs & REFs Adapter",
    "Reference Creator",
    "CVs Extractor & Mapper"
])

# --- HEADER ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image(
        "https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y",
        width=140
    )
with col2:
    st.markdown("## AO Tools Dashboard")
    st.write("Smart automation tools for project references & resumes")

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
