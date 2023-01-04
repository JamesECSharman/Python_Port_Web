import streamlit as st

st.header("Contact Me")

with st.form('email_form', clear_on_submit=True):
    user_email = st.text_input("Enter your email address below")
    user_message = st.text_area("Enter your message below")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        user_message = user_message + user_email
        
