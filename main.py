import streamlit as st
from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

# 1) Page config + wide layout + icon
st.set_page_config(
    page_title="🧰 AO Tools Dashboard",
    page_icon="🧰",
    layout="wide"
)

# 2) Sidebar navigation instead of tabs
st.sidebar.title("🔧 AO Tools")
choice = st.sidebar.radio(
    "Select a tool",
    ("CVs & REFs Adapter", "Reference Creator", "CVs Extractor")
)

# 3) Header area with logo + title
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://i.imgur.com/4AiXzf8.png", width=80)  # your logo url
with col2:
    st.markdown("<h1 style='margin-bottom: 0'>🧰 AO Tools Dashboard</h1>", unsafe_allow_html=True)
    st.caption("Pick a tool from the sidebar and get going!")

st.markdown("---")  # horizontal divider

# 4) Run the right app in the main area
if choice == "CVs & REFs Adapter":
    st.header("🔁 CVs & REFs Adapter")
    st.write("Adapt your references and CVs in one place.")
    run_cvs_refs_adapter()

elif choice == "Reference Creator":
    st.header("🧠 Reference Creator")
    st.write("Generate bilingual reference docs from any report.")
    run_ref_creator()

else:
    st.header("📄 CVs Section Extractor & Mapper")
    st.write("Map resume sections into your custom template.")
    run_cvs_adapter()
