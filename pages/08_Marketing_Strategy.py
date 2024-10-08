import streamlit as st
from streamlit_function import func

st.set_page_config(page_title="마케팅 전략", layout="wide")

st.title("마케팅 전략")

tab = st.tabs(['도출 결과', '데이터 준비', '마케팅'])

with tab[0]:
    st.text('멤버십 기간, 전 달 이용횟수, 정기이용여부')

with tab[-1]:
    st.subheader("Marketing")

    radio_marketing = st.radio(label='marketing', label_visibility='collapsed', horizontal=True, options=["온라인 마케팅", "오프라인 마케팅"])
    
    if radio_marketing == '온라인 마케팅':
        st.text("홈페이지 서비스, 이벤트, 이메일")

    elif radio_marketing == '오프라인 마케팅':
        st.text("전단지, 프로모션 및 할인")
