import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="📄",
    layout="wide"
)

# === STYLES ===
st.markdown("""

    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    
    <style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
        min-width: 300px;
        width: 300px;
        border-right: 2px solid #dee2e6; 
    }

    /* Sidebar logo */
    /* Sidebar logo */
    [data-testid="stSidebar"] img {
        display: block;
        margin: 2rem auto 1rem auto;
        width: 180px;
    }


    /* Page title */
    .centered-title {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        color: #1d3557;
        margin-bottom: 0.2rem;
        font-family: 'Comic Sans MS', 'Comic Neue', cursive;
    }
    .subtitle {
        text-align: center;
        color: #6c757d;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }

    /* Radio layout */
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

    /* Blue dot */
    /* Make the actual dot inside the radio blue */
    .stRadio input[type="radio"] + div svg {
        fill: #339af0 !important;
    }


    /* Selected effect */
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
    st.image("https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y")
    choice = st.radio("Choose a tool", [
        "CVs & REFs Adapter",
        "Reference Creator",
        "CVs Extractor & Mapper"
    ])

# === HEADER ===
st.markdown("<div class='centered-title'>AO Tools Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart automation tools for project references & resumes</div>", unsafe_allow_html=True)
st.markdown("---")

# === MAIN ===
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
