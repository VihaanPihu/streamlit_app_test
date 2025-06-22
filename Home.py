import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Main Home", layout="centered")

st.title("📚 Welcome to the Learning App!")
st.write("Use the sidebar to navigate to different pages.")

image_path = Path(__file__).parent/"family.jpeg"
st.image(image_path)
