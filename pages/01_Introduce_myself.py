import streamlit as st

st.set_page_config(page_title="자기소개", layout="wide")

st.title("자기소개")

st.subheader("인적사항")
st.markdown("이름 : **윤선준**")
st.text("생년월일 : 1997.04.17")
st.text("이메일 주소 : saro97@naver.com, ehild97@gmail.com")
st.markdown("**현재 세종교육에서 직업훈련(인공지능) 중**")

st.markdown("\n")

st.subheader("프로그래밍")
st.markdown("주로 사용하는 프로그래밍 언어 : C++, C#, **Python**, Java, Kotlin")
st.text("사용 가능한 프로그래밍 언어 : JavaScript, dart, Go, Ruby")
st.text("etc : html, css, Unity")

st.markdown("\n")

st.subheader("그 외")

st.link_button("Go to other homepage", "https://aroa97.github.io/Web/MyWeb/html/Main.html")
st.image("./images/background_image.png", width=600)
