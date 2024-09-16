import streamlit as st
import pandas as pd

# 페이지 이름 설정
st.set_page_config(page_title="데이터 전처리", layout="wide")

st.title("데이터 전처리")

tab = st.tabs(["데이터베이스", "데이터 결합", "데이터 가공", "데이터 요약", "상관관계", "히스토그램", "통계"])

with tab[0]:
    st.subheader("데이터베이스")
    st.text("MySQL 사용")
    st.image("./images/mysql_insert_data.png")
with tab[1]:
    st.subheader("데이터 결합")
    st.text("MySQL join")

    col1, _ = st.columns(2)
    with col1:
        tab_join = st.tabs(['customer_master + class_master', "customer_join + campaign_master"])
        with tab_join[0]:
            st.text("고양이")
with tab[2]:
    st.subheader("데이터 가공")
    st.text("올빼미")
with tab[3]:
    st.subheader("데이터 요약")
    st.text("올빼미")
with tab[4]:
    st.subheader("상관관계")
    st.text("올빼미")