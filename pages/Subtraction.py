import streamlit as st
import random

st.set_page_config(page_title="Subtraction Practice", page_icon="-")

st.title("🧒 Subtraction Practice for Nitya")

# --- Difficulty selector ---
difficulty = st.radio("Choose number type:", ["2-digit", "3-digit","4-digit","5-digit"])

# --- Helper to generate random numbers based on difficulty ---
def generate_numbers():
    if difficulty == "2-digit":
        while 1:
            t1=random.randint(10, 99)
            t2=random.randint(10, 99)
            if t1>t2:
                break
        return t1, t2
    elif difficulty == "3-digit":
        while 1:
            t1=random.randint(100, 999)
            t2=random.randint(100, 999)
            if t1>t2:
                break
        return t1, t2
    elif difficulty == "4-digit":
        while 1:
            t1=random.randint(1000, 9999)
            t2=random.randint(1000, 9999)
            if t1>t2:
                break
        return t1, t2
    else:
        while 1:
            t1=random.randint(10000, 99999)
            t2=random.randint(10000, 99999)
            if t1>t2:
                break
        return t1, t2

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
    st.code(f"{' '}{a_str}\n-{b_str}\n" + "-" * (len(a_str) + 2), language='text')
    ans1 = st.number_input("Your Answer", key="ans1", step=1,value=None)
    if st.button("✅ Check Answer", key="check1"):
        if ans1 == a - b:
            st.success("🎉 Correct!")
            st.balloons()
        else:
            st.error(f"❌ Try again. The correct answer is {a - b}")

with col2:
    st.markdown("### Problem 2")
    st.code(f"{' '}{x_str}\n-{y_str}\n" + "-" * (len(x_str) + 2), language='text')
    ans2 = st.number_input("Your Answer", key="ans2", step=1,value=None)
    if st.button("✅ Check Answer", key="check2"):
        if ans2 == x - y:
            st.success("🎉 Correct!")
            st.balloons()
        else:
            st.error(f"❌ Try again. The correct answer is {x - y}")

# --- Reset button to generate new problems ---
if st.button("🔄 New Problems"):
    st.session_state.a, st.session_state.b = generate_numbers()
    st.session_state.x, st.session_state.y = generate_numbers()
    st.rerun()
