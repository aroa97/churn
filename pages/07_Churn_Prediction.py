import pandas as pd
import streamlit as st

st.set_page_config(page_title="회원탈퇴예측", layout="wide")

st.title("회원탈퇴예측")

tab = st.tabs(['데이터 준비', '모델 학습', '모델 평가'])

with tab[0]:
    st.subheader('데이터 준비')
with tab[1]:
    st.subheader('모델 학습')
with tab[2]:
    st.subheader('모델 평가')

