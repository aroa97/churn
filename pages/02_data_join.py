import streamlit as st
import pandas as pd

tab = st.tabs(["데이터베이스", "데이터 결합", "데이터 가공"])

with tab[0]:
    st.title("데이터베이스")
    st.text("고양이")
with tab[1]:
    st.title("데이터 결합")
    st.text("개")
with tab[2]:
    st.title("데이터 가공")
    st.text("올빼미")