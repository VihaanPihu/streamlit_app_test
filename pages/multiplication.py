import streamlit as st
import random

st.set_page_config(page_title="Multiplication Practice", page_icon="➕")

st.title("🧒 multiplication Practice for Nitya")

# --- Difficulty selector ---
difficulty = st.radio("Choose number type:", ["2-digit", "3-digit","4-digit","5-digit"])

# --- Helper to generate random numbers based on difficulty ---
def generate_numbers():
    if difficulty == "1-digit":
        return random.randint(1, 9), random.randint(1, 9)
    elif difficulty == "2-digit":
        return random.randint(10, 99), random.randint(10, 99)
    elif difficulty == "3-digit":
        return random.randint(100, 999), random.randint(100, 999)
    elif difficulty == "4-digit":
        return random.randint(1000, 9999), random.randint(1000, 9999)
    else:
        return random.randint(10000, 99999), random.randint(10000, 99999)

# --- Initialize session state to prevent numbers from changing ---
if "a" not in st.session_state:
    st.session_state.a, st.session_state.b = generate_numbers()
    st.session_state.x, st.session_state.y = generate_numbers()

a, b = st.session_state.a, st.session_state.b
x, y = st.session_state.x, st.session_state.y

# --- Function to align numbers based on max width ---
def align_numbers(num1, num2):
    max_width = max(len(str(num1)), len(str(num2)))
    return str(num1).rjust(max_width), str(num2).rjust(max_width)

a_str, b_str = align_numbers(a, b)
x_str, y_str = align_numbers(x, y)

# --- Display two problems side-by-side ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Problem 1")
    st.code(f"{' '}{a_str}\nx{b_str}\n" + "-" * (len(a_str) + 2), language='text')
    ans1 = st.number_input("Your Answer", key="ans1", step=1,value=None)
    if st.button("✅ Check Answer", key="check1"):
        if ans1 == a * b:
            st.success("🎉 Correct!")
            st.balloons()
        else:
            st.error(f"❌ Try again. The correct answer is {a * b}")

with col2:
    st.markdown("### Problem 2")
    st.code(f"{' '}{x_str}\nx{y_str}\n" + "-" * (len(x_str) + 2), language='text')
    ans2 = st.number_input("Your Answer", key="ans2", step=1,value=None)
    if st.button("✅ Check Answer", key="check2"):
        if ans2 == x * y:
            st.success("🎉 Correct!")
            st.balloons()
        else:
            st.error(f"❌ Try again. The correct answer is {x * y}")

# --- Reset button to generate new problems ---
if st.button("🔄 New Problems"):
    st.session_state.a, st.session_state.b = generate_numbers()
    st.session_state.x, st.session_state.y = generate_numbers()
    st.rerun()
