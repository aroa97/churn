import streamlit as st

st.set_page_config(page_title="의뢰인의 요구사항", layout="wide")

st.title("의뢰인의 요구사항")

st.markdown("가상의 의뢰인을 만들어 그 의뢰인의 요구사항에 응대하자.")

st.subheader("요구사항")

radio = st.radio("", label_visibility="collapsed", options=["first", "second", "third"], horizontal=True)

if radio == "first":
    st.text("기업에서 운영하는 스포츠 센터는 트레이닝 붐 덕분에 지금까지 고객 수가 늘었습니다.")
    st.text("그런데 최근 1년간 고객 수가 늘지 않는 것 같습니다. 자주 이용하는 고객은 계속 오지만")
    st.text("가끔 오는 고객은 어느새 오지 않는 경우도 생기는 것 같습니다. 제대로 데이터를 분석한 적이 없어서")
    st.text("어떤 고객이 계속 이용하고 있는지조차 모릅니다. 데이터 분석을 하면 뭔가 알 수 있을 까요?")

    st.markdown("\n")
    
    st.markdown("**데이터 분석을 통한 헬스장 회원의 모습 파악**")

elif radio == "second":
    st.text("고객별로 이용 경향이 다르기 때문에 이런 경향을 분석해서 고객별 이용 횟수 같은 것도 예측할 수 있을까요?")

    st.markdown("\n")
    
    st.markdown("**머신러닝을 통한 헬스장 회원 이용 횟수 예측**")

elif radio == "third":
    st.text("잘 생각해보면 회원을 정착시키고 늘려가는 것보다 탈퇴를 막는 것이 중요한 것 같습니다. 탈퇴 이유를 알 수 있나요?")

    st.markdown("\n")
    
    st.markdown("**머신러닝을 통한 헬스장 회원 탈퇴 예측**")