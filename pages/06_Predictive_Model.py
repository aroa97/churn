import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from pyecharts import options as opts
from pyecharts.charts import Bar
# from pyecharts.charts import Scatter
import streamlit.components.v1 as components


st.set_page_config(page_title="예측 모델", layout="wide")

st.title("예측 모델")

df_customer = pd.read_csv("./database/customer_join.csv", encoding="cp949")

tab = st.tabs(['그룹화', '그룹화 결과 분석', '그룹화 결과 시각화', "선형회귀모델"])

customer_clustering = df_customer[['mean', 'median', 'max', 'min', 'membership_period']]
sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering.loc[:, "cluster"] = clusters.labels_
customer_clustering.columns = ["월평균값", "월중앙값", "월최댓값", "월최솟값","회원기간", "cluster"]

# 주성분 분석   
X = customer_clustering_sc
pca = PCA(n_components=2, random_state=0)
pca.fit(X)
                    
x_pca = pca.transform(X)
pca_df = pd.DataFrame(x_pca)
pca_df["cluster"] = customer_clustering["cluster"]

with tab[0]:
    st.subheader("그룹화")
    st.text("데이터를 분석하고 이해하기 위한 clustering")

    radio_cluster = st.radio(label="", label_visibility='collapsed', options=["데이터", "데이터 표준화", "KMeans"], horizontal=True)

    if radio_cluster == "데이터":
        st.dataframe(df_customer[['mean', 'median', 'max', 'min', 'membership_period']], width=800)
        
    elif radio_cluster == "데이터 표준화":

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(customer_clustering_sc, use_container_width=True)
            
        with col2 :
            _, col3, _ = st.columns(3)
            with col3:
                st.markdown("""**Standardization**
                            \n- 정규 분포화 
                            \n- 스케일 조정
                            \n- 모델 성능 향상
                            \n- 훈련 속도 개선
                            \n- 노이즈 감소
                            \n- 일관성 유지
                """) 
        with st.expander("Source Code"):
            st.code('''
from sklearn.preprocessing import StandardScaler
                        
df_customer = pd.read_csv("./database/customer_join.csv", encoding="cp949")

customer_clustering = df_customer[['mean', 'median', 'max', 'min', 'membership_period']]
sc = StandardScaler()
                        
customer_clustering_sc = sc.fit_transform(customer_clustering)
''')
    elif radio_cluster == "KMeans":

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(customer_clustering, use_container_width=True)

        with col2:
            st.markdown("""**KMeans**
                        \n 기본원리
                        \n- **클러스터 중심** : KMeans는 각 클러스터의 중심(centroid)을 계산하고, 데이터 포인트를 가장 가까운 클러스터 중심에 할당합니다.
                        \n- **반복적 과정** : 클러스터 중심을 업데이트하고, 각 데이터 포인트의 할당을 반복하여 클러스터가 더 이상 변하지 않을 때까지 수행합니다.""")
        with st.expander("Source Code"):
            st.code('''
from sklearn.cluster import KMeans
                    
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering.loc[:, "cluster"] = clusters.labels_
customer_clustering.columns = ["월평균값", "월중앙값", "월최댓값", "월최솟값","회원기간", "cluster"]
''')
with tab[1]:
    st.subheader("그룹화 결과 분석")

    col1, col2, _ = st.columns(3)

    with col1:
        st.markdown('\n')
        st.markdown('\n')
        st.markdown('\n')
        st.markdown('\n')
        st.markdown('\n')
        st.dataframe(customer_clustering.groupby("cluster").mean(), use_container_width=True)
    with col2:
        cluster_mean = customer_clustering.groupby("cluster").mean()

        c = (Bar()
            .add_xaxis(["0 group", "1 group", "2 group", "3 group"])
            .add_yaxis('mean', list(np.round(cluster_mean.loc[:, "월평균값"].values, 2)))
            .add_yaxis('median', list(np.round(cluster_mean.loc[:, "월중앙값"].values, 2)))
            .add_yaxis('max', list(np.round(cluster_mean.loc[:, "월최댓값"].values, 2)))
            .add_yaxis('min', list(np.round(cluster_mean.loc[:, "월최솟값"].values, 2)))
            .add_yaxis('membership_period', list(np.round(cluster_mean.loc[:, "회원기간"].values, 2)))
            .set_global_opts(title_opts=opts.TitleOpts(title=f"Group Total", subtitle=""),
                             toolbox_opts=opts.ToolboxOpts())
            .render_embed() # generate a local HTML file
        )
        components.html(c, width=1000, height=1000)
with tab[2]:
    st.subheader("그룹화 결과 시각화")

    st.text("차원 축소 후 시각화")

    radio_pca = st.radio(label="", label_visibility='collapsed', options=["PCA", "시각화"], horizontal=True)

    if radio_pca == "PCA":
        col1, col2 = st.columns(2)
    
        with col1:
            st.dataframe(pca_df, use_container_width=True)
        with col2:
            st.markdown(""" **주성분 분석**(Principal Component Analysis, PCA)
                        \n- 정보 압축 : 데이터의 주요 정보를 유지하면서 차원을 줄입니다.
                        \n- **시각화** : 고차원 데이터를 2D 또는 3D로 시각화할 수 있습니다.
                        \n- 노이즈 제거 : 불필요한 정보(노이즈)를 제거하여 모델 성능을 향상시킬 수 있습니다.
                        """)
        with st.expander("Source Code"):
            st.code('''
from sklearn.decomposition import PCA
                    
X = customer_clustering_sc
pca = PCA(n_components=2, random_state=0)
pca.fit(X)
                    
x_pca = pca.transform(X)
pca_df = pd.DataFrame(x_pca)
pca_df["cluster"] = customer_clustering["cluster"]
''')
    elif radio_pca == "시각화":

        col1, col2, _ = st.columns(3)
        
        with col1:
            plt.clf()

            color = ['red', 'orange', 'green', 'blue']

            for i in customer_clustering["cluster"].unique():
                tmp = pca_df.loc[pca_df["cluster"]==i]
                plt.scatter(tmp[0], tmp[1], c=color[i])
            for i in range(4):
                plt.scatter([],[],c=color[i], label=f"{i} Group")
            plt.legend(loc='upper right')

            st.pyplot(plt)
            
            # st.markdown("""
            #             \n- 0 Group : :red[빨강]
            #             \n- 1 Group : :orange[주황]
            #             \n- 2 Group : :green[초록]
            #             \n- 3 Group : :blue[파랑]
            #             """)

            # p = (Scatter()
            #      .add_xaxis(list(np.round(pca_df.iloc[:, 0], 2)))
            #      .add_yaxis('y', list(np.round(pca_df.iloc[:, 1], 2)))
            #      .set_global_opts(
            #                       xaxis_opts=opts.AxisOpts(min_=-10, max_=10, max_interval=0.1),  # y축 간격 설정
            #                       title_opts=opts.TitleOpts(title=f"Group Scatter", subtitle=""),
            #                       toolbox_opts=opts.ToolboxOpts())
            #      .render_embed() # generate a local HTML file
            # )
            # components.html(p, width=1000, height=1000)

        with col2:
            cluster_mean = customer_clustering.groupby("cluster").mean()

            c = (Bar()
                .add_xaxis(["0 group", "1 group", "2 group", "3 group"])
                .add_yaxis('mean', list(np.round(cluster_mean.loc[:, "월평균값"].values, 2)))
                .add_yaxis('median', list(np.round(cluster_mean.loc[:, "월중앙값"].values, 2)))
                .add_yaxis('max', list(np.round(cluster_mean.loc[:, "월최댓값"].values, 2)))
                .add_yaxis('min', list(np.round(cluster_mean.loc[:, "월최솟값"].values, 2)))
                .add_yaxis('membership_period', list(np.round(cluster_mean.loc[:, "회원기간"].values, 2)))
                .set_global_opts(title_opts=opts.TitleOpts(title=f"Group Total", subtitle=""),
                                 toolbox_opts=opts.ToolboxOpts())
                .render_embed() # generate a local HTML file
            )
            components.html(c, width=1000, height=1000)

from dateutil.relativedelta import relativedelta
    


with tab[3]:
    st.subheader("선형회귀모델")
    st.text("회원의 이용 횟수 예측")

    predict_data = pd.read_csv('./database/predict_data.csv', encoding='cp949')

    radio_linear = st.radio(label="", label_visibility='collapsed', options=["데이터 준비", "모델 학습", "모델 평가", "데이터 업로드"], horizontal=True)

    if radio_linear == "데이터 준비":
        st.dataframe(predict_data, use_container_width=True)
        with st.expander("Source Code"):
            st.code('''
import pandas as pd
from dateutil.relativedelta import relativedelta
    
df_uselog = pd.read_csv('./database/use_log.csv')

customer_clustering = pd.concat([customer_clustering, df_customer], axis=1)

df_uselog["usedate"] = pd.to_datetime(df_uselog["usedate"])
df_uselog["연월"] = df_uselog["usedate"].dt.strftime("%Y%m")
df_uselog_months = df_uselog.groupby(["연월", 'customer_id'],as_index=False).count()
df_uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del df_uselog_months["usedate"]
year_months = list(df_uselog_months["연월"].unique())

predict_data = pd.DataFrame()
for i in range(6, len(year_months)):
    tmp = df_uselog_months.loc[df_uselog_months["연월"]==year_months[i]]
    tmp = tmp.rename(columns={"count":"count_pred"})

    for j in range(1, 7):
        tmp_before = df_uselog_months.loc[df_uselog_months["연월"]==year_months[i-j]]
        del tmp_before["연월"]
        tmp_before = tmp_before.rename(columns={"count":"count_{}".format(j-1)})
        tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
    predict_data = pd.concat([predict_data, tmp], ignore_index=True)
predict_data = predict_data.dropna()
predict_data = predict_data.reset_index(drop=True)
    
predict_data = pd.merge(predict_data, df_customer[["customer_id","start_date"]], on="customer_id", how="left")
predict_data["now_date"] = pd.to_datetime(predict_data["연월"], format="%Y%m")
predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
predict_data["period"] = None
for i in range(len(predict_data)):
    delta = relativedelta(predict_data["now_date"][i], predict_data["start_date"][i])
    predict_data.iloc[i, -1] = delta.years*12 + delta.months
predict_data = predict_data.loc[predict_data["start_date"]>=pd.to_datetime("20180401")]
''')
    elif radio_linear == "모델 학습":
        st.code('''
from sklearn import linear_model
import sklearn.model_selection

model = linear_model.LinearRegression()
                    
X = predict_data[["count_0","count_1","count_2","count_3","count_4","count_5","period"]]
y = predict_data["count_pred"]
                    
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, shuffle=True)
model.fit(X_train, y_train)
                    
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
''')
    elif radio_linear == "모델 평가":
        col1, col2 = st.columns(2)
        with col1:
            st.image('./streamlit_images/python/python_model_score.png', width=300)
            st.image('./streamlit_images/python/python_model_predict.png', width=500)
            st.image('./streamlit_images/python/python_model_predict2.png', use_column_width=True)
        with col2 :
            st.image('./streamlit_images/python/python_linear_model_coef.png', width=400)

    elif radio_linear == "데이터 업로드":
        st.image('./streamlit_images/mysql/mysql_create_use_log_months.png', width=800)
        with st.expander("Source Code"):
            st.code('''
import pandas as pd
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
        conn.execute((text)(f"DROP TABLE IF EXISTS use_log_months;"))

        create_use_log_months_table = """
        CREATE TABLE IF NOT EXISTS use_log_months(
            연월 char(8) NOT NULL,
            customer_id VARCHAR(20) NOT NULL,
            count int NOT NULL
        );
        """

        # 테이블 만들기
        conn.execute(text(create_use_log_months_table))

        # Dataframe.to_sql을 사용해서 데이터 넣기
        df_uselog_months.to_sql("use_log_months", con=engine, index=False, if_exists="append", method="multi")
    
except Exception as e:
        print(f"Error: {e}")

# Connection 닫기
engine.dispose()
''')