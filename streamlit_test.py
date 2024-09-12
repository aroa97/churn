import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.pyplot as plt

# 페이지 이름 설정
st.set_page_config(page_title="헬스장 회원탈퇴 예측", layout="wide")

# DB 정보 정의, 엔진 생성
db_user = "root"
db_password = "12341234"
db_host = "localhost"
db_port = "3306"
db_name = "churn_db"

# engine = create_engine(
#     f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# )

# 사이드바를 통해 페이지 선택
st.sidebar.title("목록")
page = st.sidebar.radio(
    "페이지를 선택하세요:", ["회원 데이터", "데이터 가공", "탈퇴 예측", "FAQ"])
    
def data_page_func(data_page):
    file_name_paths = f'./data/{data_page}.csv'
    if file_name_paths:
        try:
            # 엑셀 파일을 데이터프레임으로 읽기
            dfx = pd.read_csv(file_name_paths)

            # 데이터프레임 표시
            st.write("customer_master")
            st.dataframe(dfx, width=1250)
        except FileNotFoundError:
            st.error("파일을 찾을 수 없습니다. 올바른 파일명을 입력했는지 확인하세요.")
        except Exception as e:
            st.error(f"파일을 불러오는 중 오류가 발생했습니다: {e}")

# 각 페이지의 내용 정의
if page == '회원 데이터':
    st.title("데이터")
    st.sidebar.title("제공 받은 데이터")
    
    data_page = st.sidebar.radio("4개의 csv 데이터", ["customer_master", "class_master", "campaign_master", 'use_log'])

    data_page_func(data_page)
    