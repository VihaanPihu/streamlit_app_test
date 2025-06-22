import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="Multiplication Table Generator", page_icon="🧮", layout="centered")

# Title with emoji
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧮 Multiplication Table Generator</h1>", unsafe_allow_html=True)

# Number input with helpful caption
st.markdown("### ➕ Enter a number to generate its multiplication table:")
num = st.number_input("Choose a number", min_value=1, max_value=1000, value=5, step=1)

# Generate table
table_data = {
    "Expression": [f"{num} × {i}" for i in range(1, 11)],
    "Result": [num * i for i in range(1, 11)]
}
df = pd.DataFrame(table_data)
df.set_index("Expression",inplace=True)

# Spacer
st.markdown("---")

# Display the table nicely
st.markdown(f"### 📋 Multiplication Table of {num}")
st.table(df)

# Optional footer
st.markdown("<div style='text-align: center; color: grey; margin-top: 50px;'>Built with ❤️ (Jhumma)</div>", unsafe_allow_html=True)
