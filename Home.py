import streamlit as st
import pandas

# set page config to wide
st.set_page_config(
    layout='wide'
)

# Prepare the columns for use
col1, col2 = st.columns([0.75, 1.25])

# Add image to the first column
with col1:
    st.image("images/photo.jpeg", width=400, use_column_width=True)

# Add content to the second column
with col2:
    st.title("James Sharman")
    content = """Hi! I am James, and welcome to my Python portfolio. I currently work as a Head of Product Solutions, 
    managing a team of technical architects and product solution managers.
    This portfolio demonstrates some of my technical abilities, born from my love to continue to learn and grow.  """
    st.info(content)

# Define content for the segment below the first two columns
content_2 = """
You can find some of the apps I have built in Python below. Feel free to contact me!
"""

# Display content below the first two columns
st.subheader(content_2)

# Read csv file
df = pandas.read_csv("data.csv", sep=";")

# Prepare the columns for use, empty column is for the purposes of spacing
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Add content to the third column
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')

# Add content to the fourth column
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')