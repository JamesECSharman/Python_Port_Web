import streamlit as st
import pandas

st.set_page_config(
    layout='wide'
)

col1, col2 = st.columns([0.75, 1.25])

with col1:
    st.image("images/photo.jpeg", width=400, use_column_width=True)

with col2:
    st.title("James Sharman")
    content = """Hi! I am James, and welcome to my Python portfolio. I currently work as a Head of Product Solutions, managing a team of technical architects and product solution managers. 
    This portfolio demonstrates some of my technical abilities, born from my love to continue to learn and grow.  """
    st.info(content)


content_2 = """
You can find some of the apps I have built in Python below. Feel free to contact me!
"""

df = pandas.read_csv("data.csv", sep=";")

with open("data.csv") as file:
    content=file.read()

st.subheader(content_2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')