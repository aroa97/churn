import streamlit as st
import pandas as pd

# 페이지 이름 설정
st.set_page_config(page_title="개발환경", layout="wide")

st.title("개발환경")

# 가상 환경 관리 : anaconda3
# 데이터 분석 : Pandas, Numpy
# 데이터 시각화 : Matplotlib, Seaborn
# 데이터베이스 : MySQL, Oracle
# 머신 러닝 및 딥 러닝 : scikit-learn, TensorFlow(Keras)
# 웹 App : Streamlit(Github 연동)

tab = st.tabs(["가상 환경 관리", "데이터 분석", "데이터 시각화", "데이터 베이스", "머신 러닝 및 러닝", "웹 App"])

with tab[0]:
    st.subheader("가상 환경 관리")
with tab[1]:
    st.subheader("데이터 분석")
with tab[2]:
    st.subheader("데이터 시각화")
with tab[3]:
    st.subheader("데이터 베이스")
with tab[4]:
    st.subheader("머신 러닝 및 러닝")
with tab[5]:
    st.subheader("웹 App")