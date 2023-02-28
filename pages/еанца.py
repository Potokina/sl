

import streamlit as st
from PIL import Image
img = Image.open("евчвап.jpg")
st.image(img, width=800)