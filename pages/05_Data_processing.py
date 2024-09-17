import streamlit as st

# 페이지 이름 설정
st.set_page_config(page_title="데이터 전처리", layout="wide")

st.title("데이터 전처리")

tab = st.tabs(["데이터베이스", "데이터 결합", "데이터 가공", "데이터 요약", "상관관계", "히스토그램", "통계"])

with tab[0]:
    st.subheader("데이터베이스")
    st.text("MySQL 사용")
    st.image("./images/mysql_insert_data.png", width=600)
    st.code('''import pandas as pd
from sqlalchemy import create_engine, text
            
customer_csv_file_path = (
    r"./data/customer_master.csv"
)
df_customer = pd.read_csv(customer_csv_file_path, encoding='cp949')
class_csv_file_path = (
    r"./data/class_master.csv"
)
df_class = pd.read_csv(class_csv_file_path)
campaign_csv_file_path = (
    r"./data/campaign_master.csv"
)
df_campaign = pd.read_csv(campaign_csv_file_path)
use_log_csv_file_path = (
    r"./data/use_log.csv"
)
df_use_log = pd.read_csv(use_log_csv_file_path)

# MySQL connection 세팅
db_user = "root"
db_password = "####"
db_host = "localhost"
db_port = "3306"
db_name = "churn_db"

# SQLAlchemy 엔진 생성 (데이터베이스 생성 전용)
create_engine_without_db = create_engine(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}"
)

# 데이터베이스 생성
with create_engine_without_db.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name};"))

    # SQLAlchemy 엔진 생성
    engine = create_engine(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
try:
    with engine.connect() as conn:
        conn.execute(text(f"USE {db_name};"))

        table_names = ['customer_master', 'class_master', 'campaign_master', 'use_log']

        # 중복되지 않도록 테이블 DROP하기
        for i in range(len(table_names)):
            conn.execute((text)(f"DROP TABLE IF EXISTS {table_names[i]};"))

        create_customer_table = """
        CREATE TABLE IF NOT EXISTS customer_master(
            customer_id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            class VARCHAR(20) NOT NULL,
            gender varchar(5),
            start_date date NOT NULL,
            end_date date,
            campaign_id VARCHAR(20) NOT NULL,
            is_deleted boolean
        );
        """

        create_class_table = """
        CREATE TABLE IF NOT EXISTS class_master(
            class VARCHAR(20) NOT NULL,
            class_name VARCHAR(20) NOT NULL,
            price int NOT NULL
        );
        """
        create_campaign_table = """
        CREATE TABLE IF NOT EXISTS campaign_master(
            campaign_id VARCHAR(20) NOT NULL,
            campaign_name VARCHAR(20) NOT NULL
        );
        """
        create_use_log_table = """
        CREATE TABLE IF NOT EXISTS use_log(
            log_id VARCHAR(20) PRIMARY KEY,
            customer_id VARCHAR(20),
            usedate date NOT NULL
        );
        """

        # 테이블 만들기
        conn.execute(text(create_customer_table))
        conn.execute(text(create_class_table))
        conn.execute(text(create_campaign_table))
        conn.execute(text(create_use_log_table))

        # Dataframe.to_sql을 사용해서 데이터 넣기
        df_customer.to_sql(table_names[0], con=engine, index=False, if_exists="append", method="multi")
        df_class.to_sql(table_names[1], con=engine, index=False, if_exists="append", method="multi")
        df_campaign.to_sql(table_names[2], con=engine, index=False, if_exists="append", method="multi")
        df_use_log.to_sql(table_names[3], con=engine, index=False, if_exists="append", method="multi")
    
except Exception as e:
        print(f"Error: {e}")

# Connection 닫기
engine.dispose()
            ''')
with tab[1]:
    st.subheader("데이터 결합")
    st.text("MySQL join")

    col1, _ = st.columns(2)
    with col1:
        tab_join = st.tabs(['customer_master + class_master', "customer_join + campaign_master"])
        with tab_join[0]:
            st.text("고양이")
with tab[2]:
    st.subheader("데이터 가공")
with tab[3]:
    st.subheader("데이터 요약")
with tab[4]:
    st.subheader("상관관계")