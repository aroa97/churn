import streamlit as st
from PIL import Image
from pathlib import Path

def set_title(file):
    file_name = Path(file).name[3:-3].replace("_", " ")

    st.set_page_config(page_title=file_name, layout="wide")
    st.title(file_name)

def image_resize(img_name, file, hsize):
    path = './streamlit_images/' + Path(file).name[3:-3].lower() + "/" + img_name
    image = Image.open(path)
    w, h = image.size
    w *= hsize / h
    
    st.image(path, width=int(w))