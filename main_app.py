import streamlit as st
from PIL import Image 

st.title('ムサシアプリ')
st.caption('これはムサシのテストアプリです')

image = Image.open('./data/男の子.jpg')
st.image(image, width=200)