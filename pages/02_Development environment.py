import streamlit as st

# 페이지 이름 설정
st.set_page_config(page_title="개발환경", layout="wide")

st.title("개발환경")

# 가상 환경 관리 : anaconda3
# 데이터 분석 : Pandas, Numpy
# 데이터 시각화 : Matplotlib, Seaborn
# 데이터베이스 : MySQL, Oracle
# 머신 러닝 및 딥 러닝 : scikit-learn, TensorFlow(Keras)
# 웹 App : Streamlit(Github 연동)

tab = st.tabs(["사용한 프로그래밍 언어", "가상 환경 관리", "데이터 분석", "데이터 시각화", "데이터베이스", "머신 러닝 및 러닝", "웹 App"])

with tab[0]:
    st.subheader("사용한 프로그래밍 언어")
    st.text("Python")
    col1, _ = st.columns(2)
    with col1 :
        st.image("./images/python_logo.png", use_column_width=True)

with tab[1]:
    st.subheader("가상 환경 관리")
    st.text("아나콘다(anaconda)")
    col1, _ = st.columns(2)
    with col1 :
        st.image("./images/anaconda_logo.png", use_column_width=True)
with tab[2]:
    st.subheader("데이터 분석")
    st.text("Pandas, Numpy")
    col1, col2 = st.columns(2)
    with col1 :
        st.image("./images/pandas_logo.jpg", width=400)
    with col2 :
        st.image("./images/numpy_logo.png", width=250)
with tab[3]:
    st.subheader("데이터 시각화")
    st.text("Matplotlib, Seaborn, Mlxtend")
    col1, col2, col3, _ = st.columns(4)
    with col1 :
        st.image("./images/matplotlib_logo.png", width=250)
    with col2 :
        st.image("./images/seaborn_logo.png", width=250)
    with col3 :
        st.markdown("\n")
        st.markdown("\n")

        st.image("./images/mlxtend_logo.png", width=400)

with tab[4]:
    st.subheader("데이터베이스")
    st.markdown("**MySQL**, Oracle")

    col1, col2, _ = st.columns(3)
    with col1 :
        # st.markdown("""
        #             <div style="text-align: center;">
        #             <img src="./images/mysql_logo.png", width="300">
        #             </div>
        #             """, unsafe_allow_html=True)
        st.image("./images/mysql_logo.png", width=300)
    with col2 :
        # st.markdown("""
        #             <div style="text-align: center;">
        #             <img src="./images/oracle_logo.png", width="400">
        #             </div>
        #             """, unsafe_allow_html=True)
        st.image("./images/oracle_logo.png", width=500)
with tab[5]:
    st.subheader("머신 러닝 및 러닝")
    st.markdown("**Scikit-learn**, **TensorFlow**(Keras)")
    col1, col2 = st.columns(2)
    with col1 :
        st.image("./images/scikit_learn_logo.png", width=400)
    with col2 :
        st.image("./images/tensorflow_logo.png", width=400)
with tab[6]:
    st.subheader("웹 App")
    st.markdown("**Streamlit**")
    col1, _ = st.columns(2)
    with col1 :
        st.image("./images/streamlit_logo.png", use_column_width=True)