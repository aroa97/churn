import streamlit as st
from streamlit_function import func

func.set_title(__file__)

tab = st.tabs(["ChatBot", 'LangChain', 'WebServer', 'DataBase'])

with tab[0]:
    st.subheader("ChatBot")
    st.markdown("https://huggingface.co/spaces/ehild97/SDTest")

    st.image("./streamlit_images/future_plans/stable_diffusion.png", use_column_width=True)
with tab[1]:
    st.subheader("LangChain")

    col1, _, _, col2, _  = st.columns(5)

    with col1:
        func.image_resize("langchain_architecture.png", __file__, 400)
    with col2:
        st.markdown("\n")
        st.image("./streamlit_images/future_plans/langchain_logo.png", use_column_width=True)
        st.markdown("\n")
        st.image("./streamlit_images/future_plans/openai_logo.png", use_column_width=True)
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
with tab[3]:
    st.header("DataBase")

    radio_database = st.radio(label='database', label_visibility='collapsed', horizontal=True, options=['database', 'ERD'])

    if radio_database == 'database':

        col1, col2, col3 = st.columns(3)

        with col1:
            st.text("MySQL")
            st.image('./streamlit_images/future_plans/mysql_workbench.png', use_column_width=True)
        with col2:
            st.text("Oracle")
            st.image('./streamlit_images/future_plans/oracle_sqldeveloper.png', use_column_width=True)
        with col3:
            st.text("MongoDB")
            st.image('./streamlit_images/future_plans/mongodb_compass.png', use_column_width=True)

    elif radio_database == "ERD":
        st.text("MySQL")
        func.image_resize("mysql_erd.png", __file__, 500)
        

