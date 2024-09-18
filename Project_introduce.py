import streamlit as st

if __name__ == "__main__":
    # 페이지 이름 설정
    st.set_page_config(page_title="헬스장 회원탈퇴 예측 프로젝트", layout="wide")

    st.title("헬스장 회원탈퇴 예측 프로젝트")

    st.markdown("\n")

    st.image("./images/background_image2.png", width=600)

    st.text("헬스장 회원의 탈퇴 가능성을 예측하고 이를 통해 헬스장 운영자는 회원의 이탈을 사전에 파악하고,")
    st.text("적절한 고객 유지 전략을 수립하여 회원 충성도를 높이고 비즈니스 성과를 개선할 수 있습니다.")