import streamlit as st
import pandas as pd

def data_page_func(data_selectbox):
    file_name_paths = f'./data/{data_selectbox}.csv'
    if file_name_paths:
        try:
            # 엑셀 파일을 데이터프레임으로 읽기
            dfx = pd.read_csv(file_name_paths)

            # 데이터프레임 표시
            st.dataframe(dfx, width=1250, hide_index=True)
        except FileNotFoundError:
            st.error("파일을 찾을 수 없습니다. 올바른 파일명을 입력했는지 확인하세요.")
        except Exception as e:
            st.error(f"파일을 불러오는 중 오류가 발생했습니다: {e}")

# 각 페이지의 내용 정의

st.title("데이터")

col1, _ = st.columns(2)

with col1:
    data_selectbox = st.selectbox(label="", 
                                  options=["customer_master", "class_master", "campaign_master", 'use_log'], 
                                  label_visibility="collapsed")

data_page_func(data_selectbox)
