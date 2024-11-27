import streamlit as st
from ui.streamlit_app import render_main_ui

# Set up the Streamlit app
st.set_page_config(page_title="Interview Prep Tool", layout="wide")

# Render the main UI
if __name__ == "__main__":
    render_main_ui()
