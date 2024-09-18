import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input field for user's name
user_name = st.text_input("Enter your name")

# Initialize session state to store result
if 'result' not in st.session_state:
    st.session_state.result = None

# Input fields for two numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Create a row of buttons for each operation
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Add"):
        st.session_state.result = f"Dear {user_name} your result is = {num1 + num2}"
with col2:
    if st.button("Subtract"):
        st.session_state.result = f"Dear {user_name} your result is = {num1 - num2}"
with col3:
    if st.button("Multiply"):
        st.session_state.result = f"Dear {user_name} your result is = {num1 * num2}"
with col4:
    if st.button("Divide"):
        if num2 != 0:
            st.session_state.result = f"Dear {user_name} your result is = {num1 / num2}"
        else:
            st.session_state.result = f"Dear {user_name} We Cannot divide by zero"
with col5:
    if st.button("Clear"):
        st.session_state.result = "Click Any Button get Result"

# Display the result in the center with font size 20 and red color
if st.session_state.result is not None:
    st.markdown(
        f'<p style="font-size: 50px; color: red; text-align: center;">{st.session_state.result}</p>',
        unsafe_allow_html=True,
    )
