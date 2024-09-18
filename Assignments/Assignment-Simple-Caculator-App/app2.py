# check demo on this link "https://simple-cal.streamlit.app/"
import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None

st.title("Simple Calculator")

user_name = st.text_input("Enter your name")

if 'result' not in st.session_state:
    st.session_state.result = None

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Add"):
        st.session_state.result = f"Dear {user_name} your result is = {add(num1, num2)}"
with col2:
    if st.button("Subtract"):
        st.session_state.result = f"Dear {user_name} your result is = {subtract(num1, num2)}"
with col3:
    if st.button("Multiply"):
        st.session_state.result = f"Dear {user_name} your result is = {multiply(num1, num2)}"
with col4:
    if st.button("Divide"):
        result = divide(num1, num2)
        if result is not None:
            st.session_state.result = f"Dear {user_name} your result is = {result}"
        else:
            st.session_state.result = f"Dear {user_name} We Cannot divide by zero"
with col5:
    if st.button("Clear"):
        st.session_state.result = "Click Any Button get Result"

if st.session_state.result is not None:
    st.markdown(
        f'<p style="font-size: 50px; color: red; text-align: center;">{st.session_state.result}</p>',
        unsafe_allow_html=True,
    )
