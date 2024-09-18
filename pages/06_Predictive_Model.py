import numpy as np
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import streamlit.components.v1 as components


st.set_page_config(page_title="예측 모델", layout="wide")

st.title("예측 모델")

df_customer = pd.read_csv("./database/customer_join.csv", encoding="cp949")

tab = st.tabs(['그룹화', '그룹화 결과 분석', '그룹화 결과 시각화'])

customer_clustering = df_customer[['mean', 'median', 'max', 'min', 'membership_period']]
sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering.loc[:, "cluster"] = clusters.labels_
customer_clustering.columns = ["월평균값","월중앙값", "월최댓값", "월최솟값","회원기간", "cluster"]

with tab[0]:
    st.subheader("그룹화")
    st.text("데이터를 분석하고 이해하기 위한 clustering")

with tab[1]:
    st.subheader("그룹화 결과 분석")

    radio_analysis = st.radio(label="", label_visibility="collapsed", options=["집계","시각화"], horizontal=True)

    if radio_analysis == "집계":
        st.dataframe(customer_clustering.groupby("cluster").mean())
    elif radio_analysis == "시각화":
        cluster_mean = customer_clustering.groupby("cluster").mean()

        c = (Bar()
            .add_xaxis(["0 group", "1 group", "2 group", "3 group"])
            .add_yaxis('mean', list(np.round(cluster_mean.loc[:, "월평균값"].values, 2)))
            .add_yaxis('median', list(np.round(cluster_mean.loc[:, "월중앙값"].values, 2)))
            .add_yaxis('max', list(np.round(cluster_mean.loc[:, "월최댓값"].values, 2)))
            .add_yaxis('min', list(np.round(cluster_mean.loc[:, "월최솟값"].values, 2)))
            .add_yaxis('membership_period', list(np.round(cluster_mean.loc[:, "회원기간"].values, 2)))
            .set_global_opts(title_opts=opts.TitleOpts(title=f"group total", subtitle=""),
                             toolbox_opts=opts.ToolboxOpts())
            .render_embed() # generate a local HTML file
        )
        components.html(c, width=1000, height=1000)

with tab[2]:
    st.subheader("그룹화 결과 시각화")

    st.text("이상치 탐지 및 차원 축소(PCA)")
    