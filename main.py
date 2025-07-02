import streamlit as st

from CVs_REFs_adapter.app import run_app as run_cvs_refs_adapter
from REF_creater.app import run_app as run_ref_creator
from CVs_adapter.app import run_app as run_cvs_adapter

st.set_page_config(page_title="📋 AO Tools Dashboard", layout="wide")
st.title("📋 AO Tools Dashboard")

tab1, tab2, tab3 = st.tabs([
    "CVs & REFs Adapter",
    "Reference Creator",
    "CVs Adapter"
])

with tab1:
    run_cvs_refs_adapter()

with tab2:
    run_ref_creator()

with tab3:
    run_cvs_adapter()
