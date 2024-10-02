import streamlit as st
from streamlit_function import func

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

    func.image_resize("python_logo.png", __file__, 200)
    
with tab[1]:
    st.subheader("가상 환경 관리")
    st.text("Anaconda")

    func.image_resize('anaconda_logo.png', __file__, 200)

with tab[2]:
    st.subheader("데이터 분석")
    st.text("Numpy, Pandas")
    col1, col2, _, _ = st.columns(4)
    with col1 :
        func.image_resize('numpy_logo.png', __file__, 200)
    with col2 :
        func.image_resize('pandas_logo.jpg', __file__, 200)
    
    

with tab[3]:
    st.subheader("데이터 시각화")
    st.text("Matplotlib, Seaborn, Mlxtend")
    col1, col2, col3, _ = st.columns(4)
    with col1 :
        func.image_resize('matplotlib_logo.png', __file__, 200)
    with col2 :
        func.image_resize('seaborn_logo.png', __file__, 200)
    with col3 :
        func.image_resize('mlxtend_logo.png', __file__, 200)

with tab[4]:
    st.subheader("데이터베이스")
    st.markdown("MySQL, Oracle")

    col1, col2, _, _ = st.columns(4)
    with col1 :
        func.image_resize('mysql_logo.png', __file__, 200)
    with col2 :
        func.image_resize('oracle_logo.png', __file__, 200)

with tab[5]:
    st.subheader("머신 러닝 및 딥 러닝")
    st.markdown("Scikit-learn, TensorFlow")
    col1, col2, _ = st.columns(3)
    with col1 :
        func.image_resize('scikit_learn_logo.png', __file__, 200)
    with col2 :
        func.image_resize('tensorflow_logo.png', __file__, 200)

with tab[6]:
    st.subheader("웹 App")
    st.markdown("Streamlit, Jupyter")

    col1, col2, _ = st.columns(3)
    with col1:
        func.image_resize('streamlit_logo.png', __file__, 200)
    with col2:
        func.image_resize('jupyter_logo.png', __file__, 200)