import streamlit as st
from streamlit_function import func

func.set_title(__file__)

tab = st.tabs(["ChatBot", 'LangChain', 'WebServer'])

with tab[0]:
    st.subheader("ChatBot")
    st.markdown("https://huggingface.co/spaces/ehild97/SDTest")

    st.image("./streamlit_images/future_plans/stable_diffusion.png", use_column_width=True)
with tab[1]:
    st.subheader("LangChain")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("\n")
        st.image("./streamlit_images/future_plans/langchain_logo.png", use_column_width=True)
        st.markdown("\n")
        st.image("./streamlit_images/future_plans/openai_logo.png", use_column_width=True)
    with col2:
        func.image_resize("pdf.png", __file__, 150)
with tab[2]:
    st.header("WebServer")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('./streamlit_images/future_plans/aws_server.png', use_column_width=True)
    with col2:
        st.image('./streamlit_images/future_plans/aws_server_web.png', use_column_width=True)
    with col3:
        func.image_resize('tomcat_logo.png', __file__, 150)
        func.image_resize('nginx_logo.png', __file__, 150)