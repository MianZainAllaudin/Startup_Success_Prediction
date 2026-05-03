"""
LaunchLyft — Startup Success Predictor
Streamlit App (Modular, Multi-Page)

Run with:  python -m streamlit run app.py
"""

import os
import streamlit as st
import joblib

from styles import GLOBAL_CSS, WELCOME_CSS
from sidebar import render_sidebar
from welcome import render_welcome
from predictor import render_predictor

# ─── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LaunchLyft — Startup Intelligence",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Inject CSS ──────────────────────────────────────────────────────────────
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
st.markdown(WELCOME_CSS, unsafe_allow_html=True)

# ─── Load model ──────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    if os.path.exists("launchlyft_model.pkl"):
        return joblib.load("launchlyft_model.pkl")
    return None

model_package = load_model()

# ─── Session state ───────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ─── Sidebar (always visible) ────────────────────────────────────────────────
render_sidebar(model_package)

# ─── Router ──────────────────────────────────────────────────────────────────
if st.session_state.page == "welcome":
    render_welcome()
else:
    render_predictor(model_package)