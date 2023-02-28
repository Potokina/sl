import base64

import streamlit as st

st.title("Hello world!")

st.write("анчоус")

st.sidebar.title("пикачу")


import streamlit as st
from PIL import Image
img = Image.open("trt.jpg")
st.image(img, width=800)



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('евчвап.jpg')