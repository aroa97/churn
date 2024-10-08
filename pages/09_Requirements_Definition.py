import streamlit as st
from streamlit_function import func
import pandas as pd

st.set_page_config("요구사항 정의", layout="wide")

st.title("요구사항 정의")

tab = st.tabs(['요구공학', '기능 요구사항', '비기능 요구사항'])

with tab[0]:
    st.subheader('Requirements Engineering')
    st.text("요구공학은 시스템 개발에 필요한 요구사항을 도출하여 문서화(명세화)하고 이를 체계적 으로 검증 및 관리를 하는 일련의 구조화된 소프트웨어 공학 활동이다.")
    func.image_resize('requirements_engineering.png', __file__, 500)

with tab[1]:
    st.subheader('Functional Requirements')
    st.text("인공지능 모델 기능 요구사항")

    columns = ['RSQ-ID', '구분', '요구사항명', '요구사항 내용', '날짜', '작성자', '필수 여부']
    df_fr = [
        ['SFR-001', '기능', 'NAN', 'NAN', '24/09/00', '윤선준', '필수'],
        ['SFR-002', '기능', 'NAN', 'NAN', '24/09/00', '윤선준', '필수']
    ]
    df_fr = pd.DataFrame(df_fr, columns=columns)

    st.dataframe(df_fr, use_container_width=True, hide_index=True)

with tab[2]:
    st.subheader('Non-Functional Requirements')
    st.text("인공지능 모델 비기능 요구사항")

    columns = ['RSQ-ID', '구분', '요구사항명', '요구사항 내용', '날짜', '작성자', '필수 여부']
    df_nfr = [
        ['PFR-001', '비기능', 'NAN', 'NAN', '24/09/00', '윤선준', '필수'],
        ['PFR-002', '비기능', 'NAN', 'NAN', '24/09/00', '윤선준', '필수']
    ]
    df_nfr = pd.DataFrame(df_nfr, columns=columns)

    st.dataframe(df_nfr, use_container_width=True, hide_index=True)