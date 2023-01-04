import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form('email_form', clear_on_submit=True):
    user_email = st.text_input("Enter your email address below")
    raw_user_message = st.text_area("Enter your message below")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}

Message: {raw_user_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully.")
