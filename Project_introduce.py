import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# 페이지 이름 설정
st.set_page_config(page_title="헬스장 회원탈퇴 예측", layout="wide")

# # DB 정보 정의, 엔진 생성
# db_user = "root"
# db_password = "12341234"
# db_host = "localhost"
# db_port = "3306"
# db_name = "churn_db"

# engine = create_engine(
#     f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# )


