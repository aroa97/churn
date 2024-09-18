import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import heatmap

# 페이지 이름 설정
st.set_page_config(page_title="데이터 분석", layout="wide")

st.title("데이터 분석")

df_customer = pd.read_csv("./database/customer_join.csv", encoding="cp949")

tab = st.tabs(["데이터베이스", "데이터 결합", "데이터 가공", "결과", "데이터 요약", "상관관계", "통계", "히스토그램"])

with tab[0]:
    st.subheader("데이터베이스")
    st.text("Python을 사용해 MySQL에 upload")
    st.image("./images/mysql/mysql_insert_data.png", width=600)

    with st.expander("Source Code"):
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
    st.text("MySQL로 데이터 join해 새로운 table 만들기")

    
    radio_join = st.radio(label="",label_visibility="collapsed", 
                          options=['customer_master + class_master', "customer_join + campaign_master"],
                          horizontal=True)
    if radio_join == "customer_master + class_master":
        st.image("./images/mysql/mysql_create_customer_join.png", use_column_width=True)
        
        with st.expander("Source Code"):
            st.code("""use churn_db;
create table customer_join as
select customer_master.customer_id, customer_master.name, 
       customer_master.class, customer_master.gender, 
       customer_master.start_date, customer_master.end_date,
       customer_master.campaign_id, customer_master.is_deleted,
       class_master.class_name, class_master.price 
from customer_master
left join class_master on customer_master.class = class_master.class;

select * from customer_join;""")
    elif radio_join == "customer_join + campaign_master":
        st.image("./images/mysql/mysql_join_campaign_master.png", use_column_width=True)
        
        with st.expander("Source Code") :
            st.code("""alter table customer_join
add column campaign_name varchar(20) not null;

SET SQL_SAFE_UPDATES = 0;
update customer_join
set campaign_name = (SELECT campaign_name FROM campaign_master WHERE customer_join.campaign_id = campaign_master.campaign_id)
WHERE campaign_id IS NOT NULL;
SET SQL_SAFE_UPDATES = 1;

select * from customer_join;""")
with tab[2]:
    st.subheader("데이터 가공")

    st.text("데이터 read부터 데이터 upload까지")

    radio_data = st.radio(label="",label_visibility="collapsed", 
                          options=['data processing', 'data join', 'data processing2', "database upload"],
                          horizontal=True)
    if radio_data == 'data processing':
        radio_data2 = st.radio(label="",label_visibility="collapsed", 
                          options=['이용이력', '정기이용여부'],
                          horizontal=True)
        st.text('"use_log" data를 이용')

        if radio_data2 == '이용이력':
            st.image("./images/python/python_uselog_processing.png")

            with st.expander("Source Code"):
                st.code("""
df_log["usedate"] = pd.to_datetime(df_log["usedate"])
df_log["연월"] = df_log["usedate"].dt.strftime("%Y%m")
df_log_months = df_log.groupby(["연월","customer_id"],as_index=False).count()
df_log_months.rename(columns={"log_id":"count"}, inplace=True)
del df_log_months["usedate"]
df_log_customer = df_log_months.groupby("customer_id")["count"].agg(['mean', "median", "max", "min" ])
df_log_customer = df_log_customer.reset_index(drop=False)

df_log_customer.head()
""")
        elif radio_data2 == '정기이용여부':
            st.image("./images/python/python_uselog_processing2.png")

            with st.expander("Source Code"):
                st.code("""
df_log_weekday = df_log.groupby(["customer_id","연월","weekday"], 
                                as_index=False).count()[["customer_id","연월", "weekday","log_id"]]
df_log_weekday.rename(columns={"log_id":"count"}, inplace=True)
df_log_weekday = df_log_weekday.groupby("customer_id",as_index=False).max()[["customer_id", "count"]]
df_log_weekday["routine_flg"] = 0
df_log_weekday["routine_flg"] = df_log_weekday["routine_flg"].where(df_log_weekday["count"]<4, 1)

df_log_weekday.head()
""")

    elif radio_data == 'data join':
        st.image("./images/python/python_join.png")

        with st.expander("Source Code"):
            st.code("""
df_customer = pd.merge(df_customer, df_log_customer, on="customer_id", how="left")
df_customer = pd.merge(df_customer, df_log_weekday[["customer_id", "routine_flg"]], on="customer_id", how="left")

df_customer.head()
""")
    elif radio_data == 'data processing2':
        st.image("./images/python/python_membership_period.png")

        with st.expander("Source Code"):
            st.code("""
df_customer["end_date"] = pd.to_datetime(df_customer["end_date"])
df_customer["calc_date"] = df_customer["end_date"]
df_customer["calc_date"] = df_customer["calc_date"].fillna(pd.to_datetime("20190430"))
df_customer["membership_period"] = 0
for i in range(len(df_customer)):
    delta = relativedelta(df_customer.iloc[i]["calc_date"], df_customer.iloc[i]["start_date"])
    # -1 : 'membership_period'
    df_customer.iloc[i, -1] = delta.years*12 + delta.months
    
df_customer.head()
""")
    elif radio_data == 'database upload':
        st.image("./images/mysql/mysql_customer_join_upload.png")

        with st.expander("Source Code"):
            st.code('''
from sqlalchemy import create_engine, text
                    
db_user = "root"
db_password = "####"
db_host = "localhost"
db_port = "3306"
db_name = "churn_db"

engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

try:
    with engine.connect() as conn:

        # 중복되지 않도록 테이블 DROP하기
        conn.execute((text)(f"DROP TABLE IF EXISTS customer_join2;"))

        create_customer_join_table = """
        CREATE TABLE IF NOT EXISTS customer_join2(
            customer_id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            class VARCHAR(20) NOT NULL,
            gender varchar(5) NOT NULL,
            start_date date NOT NULL,
            end_date date,
            campaign_id VARCHAR(20) NOT NULL,
            is_deleted boolean NOT NULL,
            class_name VARCHAR(20) NOT NULL,
            price int NOT NULL,
            campaign_name VARCHAR(20) NOT NULL,
            mean float NOT NULL,
            median float NOT NULL,
            max int NOT NULL,
            min int NOT NULL,
            routine_flg boolean NOT NULL,
            calc_date date NOT NULL,
            membership_period int NOT NULL
        );
        """

        # 테이블 만들기
        conn.execute(text(create_customer_join_table))

        # Dataframe.to_sql을 사용해서 데이터 넣기
        df_customer.to_sql("customer_join2", con=engine, index=False, if_exists="append", method="multi")
    
except Exception as e:
        print(f"Error: {e}")

# Connection 닫기
engine.dispose()
''')
with tab[3]:
    st.subheader("결과")

    st.text("데이터 결합 및 가공의 결과")

    st.dataframe(df_customer)
with tab[4]:
    st.subheader("데이터 요약")

    st.text("데이터의 각 열에 대한 간단한 설명")

    data_summary = [['customer_id', '회원 id'],
                ['name', '회원 이름'],
                ['class', '반 id'],
                ['gender', '성별'],
                ['start_date', '회원 등록 일자'],
                ['end_date', '회원 탈퇴 일자'],
                ['campaign_id', '캠페인 id'],
                ['is_deleted', '탈퇴 여부'],
                ['class_name', '반(주, 야간, 종일) 명'],
                ['campaign_name', '캠페인 명'],
                ['mean', '평균 이용횟수'],
                ['median', '중앙값 이용횟수'],
                ['max', '최대 이용횟수'],
                ['min', '최소 이용횟수'],
                ['routine_flg', '정기이용여부'],
                ['calc_date', '임시 멤버십 종료 일자'],
                ['membership_period', '멤버십 기간']]
    
    st.dataframe(pd.DataFrame(data_summary, columns=["columns","explanation"]), width=500, height=633)
with tab[5]:
    st.subheader("상관관계")

    st.text("데이터의 상관관계 시각화")

    plt.clf()

    cols = ['is_deleted', 'mean', 'median', 'max', 'min', 'routine_flg', 'membership_period']
    cm = np.corrcoef(df_customer[cols].values.T)
    hm = heatmap(cm, row_names=cols, column_names=cols, cmap=plt.cm.Blues)

    st.pyplot(plt)
with tab[6]:
    st.subheader("통계")
    st.text("탈퇴회원과 지속회원의 이용횟수 및 멤버십 기간 통계")

    cols = ['mean', 'median', 'max', 'min', 'routine_flg', 'membership_period']

    col1, col2 = st.columns(2)
    with col1 :
        st.markdown("**지속회원**")
        is_deleted_f = df_customer[df_customer['is_deleted']==0][cols].describe()
        st.dataframe(is_deleted_f)
    with col2 :
        st.markdown("**탈퇴회원**")
        is_deleted_t = df_customer[df_customer['is_deleted']==1][cols].describe()
        st.dataframe(is_deleted_t)
with tab[7]:
    st.subheader("히스토그램")

    st.text("탈퇴회원과 지속회원의 이용횟수 및 멤버십 기간 히스토그램")

    cols = ['mean', 'median', 'max', 'min', 'routine_flg', 'membership_period']

    is_deleted_f = df_customer[df_customer['is_deleted']==0][cols].describe()
    is_deleted_t = df_customer[df_customer['is_deleted']==1][cols].describe()

    bar_cols = ['mean', 'min', '25%', '50%', '75%', 'max']

    radio_hist = st.radio(label="", label_visibility='collapsed',
                          options=['mean', 'median', 'max', 'min', 'membership_period'], horizontal=True)

    plt.figure(figsize=(10, 5))
    plt.bar(bar_cols, is_deleted_f[radio_hist][bar_cols].values, width=0.5, align='edge', color='orange', label='False')
    plt.bar(bar_cols, is_deleted_t[radio_hist][bar_cols].values, width=0.5, label='is_deleted_True')
    plt.legend(loc='upper left')
    st.pyplot(plt)
