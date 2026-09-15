import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="KPOT Tally", page_icon="🍽️", layout="wide")

# Streamlit adds its own padding/chrome around embedded components — hide the
# extra page padding so the app feels like a standalone page.
st.markdown(
    """
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = pathlib.Path(__file__).parent / "kpot-tracker.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1400, scrolling=True)
