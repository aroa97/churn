import streamlit as st
from streamlit_function import func

st.set_page_config(page_title="마케팅 전략", layout="wide")

st.title("마케팅 전략")

tab = st.tabs(['도출 결과', '데이터 준비'])

with tab[0]:
    st.text('멤버십 기간, 전 달 이용횟수, 정기이용여부')