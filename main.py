import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

# 1) Page config + wide layout + new icon
st.set_page_config(
    page_title="AO Tools Dashboard",
    page_icon="🚀",       # switched to a rocket
    layout="wide"
)

# 2) Sidebar navigation (no emojis here)
st.sidebar.title("AO Tools")
choice = st.sidebar.radio(
    "Select a tool",
    ("CVs & REFs Adapter", "Reference Creator", "CVs Extractor")
)

# 3) Header area with larger logo + plain title
col1, col2 = st.columns([1, 6])
with col1:
    # bump logo width to 150px
    st.image(
        "https://media.licdn.com/dms/image/v2/C560BAQEcFreaTdl3pA/company-logo_200_200/company-logo_200_200/0/1652801538847/africa_climate_solutions_logo?e=1756944000&v=beta&t=TNV2ntWdNm-mOqn81Pzfgj8_4URETN6fqNzkr48Lu5Y",
        width=150
    )
with col2:
    st.markdown("<h1 style='margin-bottom: 0'>AO Tools Dashboard</h1>", unsafe_allow_html=True)
    st.caption("Choose a tool on the left to get started")

st.markdown("---")

# 4) Main area, clean headers + descriptions (no emojis)
if choice == "CVs & REFs Adapter":
    st.header("CVs & REFs Adapter")
    st.write("Adapt reference documents and CVs to your specific AO.")
    run_cvs_refs_adapter()

elif choice == "Reference Creator":
    st.header("Reference Creator")
    st.write("Extract fields from reports and generate reference documents.")
    run_ref_creator()

else:
    st.header("CVs Section Extractor & Mapper")
    st.write("Map extracted resume sections into your custom template.")
    run_cvs_adapter()
