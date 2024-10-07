import streamlit as st

st.set_page_config(page_title="자기소개", layout="wide")

st.title("자기소개")

col1, col2 = st.columns(2)


with col1:
    st.subheader("인적사항")
    st.text("생년월일 : 1997.04.17")
    st.text("이메일 주소 : saro97@naver.com, ehild97@gmail.com")
    st.markdown("**현재 세종교육에서 직업훈련(인공지능) 중**")

    st.markdown("\n")

    st.markdown("주로 사용하는 프로그래밍 언어 : C++, C#, **Python**, Java, Kotlin")
    st.text("""
사용 가능한 프로그래밍 언어 : JavaScript, Dart, 
                           Go, Ruby""")
    st.text("""
그 외 스킬 : Scikit-learn, TensorFlow, Docker, 
            Linux, Github, MySQL, Oracle, AWS, 
            R, Html, Css, Unity""")

    st.markdown("\n")

    st.text("다른 홈페이지")

    st.markdown("https://github.com/aroa97")

    st.link_button("Go to other homepage", "https://aroa97.github.io/Web/MyWeb/html/Main.html")
    st.image("./streamlit_images/background_image.png", use_column_width=True)
