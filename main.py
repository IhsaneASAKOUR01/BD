import streamlit as st

from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

st.set_page_config(page_title="📋 AO Tools Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center;'>📋 AO Tools Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

tab1, tab2, tab3 = st.tabs([
    "🔁 CVs & REFs Adapter",
    "🧠 Reference Creator",
    "📄 CVs Adapter"
])

with tab1:
    st.subheader("🔁 CVs & REFs Adapter")
    st.markdown("Easily adapt references and CVs to your AO.")
    st.divider()
    run_cvs_refs_adapter()

with tab2:
    st.subheader("🧠 Reference Creator")
    st.markdown("Generate structured reference documents using your input.")
    st.divider()
    run_ref_creator()

with tab3:
    st.subheader("📄 CVs Section Mapper")
    st.markdown("Map and reformat CVs based on your custom template.")
    st.divider()
    run_cvs_adapter()
