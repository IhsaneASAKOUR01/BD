import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

# Page config
st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y",
    layout="wide"
)

# === Custom CSS for background, sidebar, layout ===
st.markdown("""
    <style>
        /* Background image */
        .stApp {
            background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
            background-size: cover;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #f0f2f6;
            border-right: 2px solid #ddd;
        }

        /* Header text */
        h1 {
            font-size: 3rem !important;
            color: #0c4a6e;
        }

        .header-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        /* Logo */
        .logo-container img {
            border-radius: 12px;
        }

        /* Description text */
        .caption {
            font-size: 1.1rem;
            color: #5a5a5a;
        }

        /* Section headers */
        .section-header {
            font-size: 1.7rem;
            color: #1a3d5d;
            font-weight: 600;
            margin-top: 1.5rem;
        }

        /* Divider */
        hr {
            border-top: 2px solid #ccc;
        }
    </style>
""", unsafe_allow_html=True)

# Header layout
col1, col2 = st.columns([1, 6])
with col1:
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image(
        "https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y",
        width=180
    )
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown("<h1>AO Tools Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<div class='caption'>Smart automation tools for project references & resumes</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio(
    "Choose a tool",
    ("CVs & REFs Adapter", "Reference Creator", "CVs Extractor & Mapper")
)

# Tool display
if choice == "CVs & REFs Adapter":
    st.markdown('<div class="section-header">CVs & REFs Adapter</div>', unsafe_allow_html=True)
    st.write("Automatically align reference files and CVs with a specific AO.")
    run_cvs_refs_adapter()

elif choice == "Reference Creator":
    st.markdown('<div class="section-header">Reference Creator</div>', unsafe_allow_html=True)
    st.write("Generate bilingual reference documents directly from project reports.")
    run_ref_creator()

else:
    st.markdown('<div class="section-header">CVs Section Extractor & Mapper</div>', unsafe_allow_html=True)
    st.write("Extract, map, and reformat CVs into your preferred structure.")
    run_cvs_adapter()
