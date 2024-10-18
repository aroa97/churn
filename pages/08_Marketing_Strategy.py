import streamlit as st
from streamlit_function import func

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="마케팅 전략", layout="wide")

st.title("마케팅 전략")

tab = st.tabs(['데이터 분석', "예측 모델", '마케팅'])

with tab[0]:
    st.subheader("EDA")

    radio_eda = st.radio(label="eda", label_visibility='collapsed', horizontal=True, 
                         options=["과정", "데이터 로드", "기초 통계량 확인", "결측치와 이상치 탐색", "변수 간의 관계 시각화", "변수 변환 및 생성"])
    
    df = pd.read_csv("./data/gym_churn_us.csv")

    if radio_eda == "과정":
        st.markdown("""
**EDA 과정**
\n **1. 데이터 로드**
\n- 데이터셋을 불러옵니다. (pandas를 사용하여 CSV, Excel 파일 등을 로드)

\n **2. 기초 통계량 확인**
\n- describe() 메서드를 사용하여 기초 통계량(평균, 표준편차, 최소값, 최대값 등)을 확인합니다.
\n- 데이터의 요약 정보를 확인하여 변수의 분포를 파악합니다.
                
\n **3. 결측치와 이상치 탐색**
\n- isnull() 또는 info() 메서드를 사용하여 결측치를 확인합니다.
\n- 시각화 기법(박스플롯, 히스토그램 등)을 사용하여 이상치를 찾아냅니다.
                    
\n **4. 변수 간의 관계 시각화**
\n- 산점도, 히스토그램, 바이올린 플롯, 상관 행렬 등을 사용하여 변수 간의 관계를 탐색합니다.
\n- seaborn과 matplotlib을 활용하여 시각적으로 표현합니다.
                                    
\n **5. 변수 변환 및 생성**
\n- 필요에 따라 변수를 변환하거나 새로운 변수를 생성하여 데이터 분석의 깊이를 더합니다.""")
    elif radio_eda == "데이터 로드":
        st.link_button(label='Source', url='https://www.kaggle.com/datasets/adrianvinueza/gym-customers-features-and-churn')
        st.code("""
# python jupyter notebook
import pandas as pd
                
df = pd.read_csv('./data/gym_churn_us.csv')
df.head()
""")

        # col1, col2 = st.columns(2)

        # with col1:
        #     df = pd.read_csv("./data/gym_churn_us.csv")
        #     st.dataframe(df.head())
        # with col2:
            # col_df = [["성별 (Gender)", "0 : 여자, 1 : 남자"],
            #           ["근처 위치 (Near_Location)", "사용자가 체육관이 위치한 동네에서 살거나 일하는지 여부"],
            #           ["파트너 (Partner)", "사용자가 관련된 회사에서 일하는지 여부 (체육관은 제휴된 회사의 직원이 할인을 받을 수 있도록 정보를 저장합니다)"],
            #           ["프로모션 친구 (Promo_friends)", "사용자가 친구의 프로모션 코드를 사용하여 처음 가입했는지 여부"],
            #           ["전화번호 (Phone)", "사용자가 전화번호를 제공했는지 여부"],
            #           ["계약 기간 (Contract_period)", "1, 6, 12개월 순으로 나누어져 있음"],
            #           ["그룹 방문 여부 (Group_visits)", "그룹, 개인 여부"],
            #           ["총 평균 추가 요금 (Avg_additional_charges_total)", ""],
            #           ["계약 종료까지 남은 월 수 (Month_to_end_contract)", ""],
            #           ["나이 (Age)", ""],
            #           ["가입 기간 (Lifetime)", "사용자가 체육관에 처음 등록한 이후 경과한 시간(개월 단위)"],
            #           ["총 평균 수업 빈도 (Avg_class_frequency_total)",""],
            #           ["현재 월 평균 수업 빈도 (Avg_class_frequency_current_month)",""],
            #           ["고객 이탈 (Churn)", "회원 탈퇴 여부"]]
            # st.dataframe(col_df)

        col_df = [["성별",
                   "근처 위치",
                   "파트너",
                   "프로모션 친구",
                   "전화번호",
                   "계약 기간",
                   "그룹 방문 여부",
                   "총 평균 추가 요금 ",
                   "계약 종료까지 남은 월 수",
                   "나이",
                   "가입 기간",
                   "총 평균 수업 빈도 (Avg_class_frequency_total)",
                   "현재 월 평균 수업 빈도 (Avg_class_frequency_current_month)",
                   "고객 이탈"],
                   ["0 = 여자, 1 = 남자",
                    "회원 체육관이 위치한 동네에서 살거나 일하는지 여부",
                    "회원 관련된 회사에서 일하는지 여부 (체육관은 제휴된 회사의 직원이 할인을 받을 수 있도록 정보를 저장합니다)",
                    "회원 친구의 프로모션 코드를 사용하여 처음 가입했는지 여부",
                    "회원 전화번호를 제공했는지 여부",
                    "1, 6, 12개월 순으로 나누어져 있음",
                    "그룹, 개인 여부",
                    "",
                    "",
                    "",
                    "회원 체육관에 처음 등록한 이후 경과한 시간(개월 단위)",
                    "",
                    "",
                    "회원 탈퇴 여부"]]
        col_df = pd.DataFrame(col_df, columns=["Gender", "Near_Location", "Partner", "Promo_friends", "Phone", "Contract_period", "Group_visits", "Avg_additional_charges_total", "Month_to_end_contract", "Age", "Lifetime", "Avg_class_frequency_total", "Avg_class_frequency_current_month", "Churn"])
        st.dataframe(col_df, hide_index=True)

        
        st.dataframe(df.head())

    elif radio_eda == "기초 통계량 확인":
        st.code("""
# python jupyter notebook
df.describe()
""")
        st.dataframe(df.describe())

    elif radio_eda == "결측치와 이상치 탐색":
        with st.expander("결측치"):
            st.code("""
# python jupyter notebook
# 결측치 확인
df.info()
df.isnull().sum()
# 중복 확인
df.duplicated().sum()
            """)
            col1, col2 = st.columns(2)
            with col1:
                st.image("./streamlit_images/marketing_strategy/data_info.png", use_column_width=True)
            with col2:
                func.image_resize("data_isnull_sum.png", __file__, 500)
           
        with st.expander("이상치"):
            st.code("""
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt

# 박스 플롯으로 이상치 확인
plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()
            """)
            plt.clf()
            plt.figure(figsize=(12, 6))
            sns.boxplot(data=df)
            plt.xticks(rotation=45)
            st.pyplot(plt)
        with st.expander("이상치 제거"):
            st.code("""
# python jupyter notebook
                    
# 0.25 0.75 분위수 계산
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# 이상치 범위 정의
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 이상치를 제외한 값만 dataframe에 넣기
df = df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

# 박스플롯 시각화로 잘 제거되었는지 확인
plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.show()
            """)
            # 0.25 0.75 분위수 계산
            Q1 = df.quantile(0.25)
            Q3 = df.quantile(0.75)
            IQR = Q3 - Q1

            # 이상치 범위 정의
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # 이상치를 제외한 값만 dataframe에 넣기
            # pandas의 DataFrame.any() 메서드는 데이터프레임 내의 값이 True인지 여부를 확인하는 데 사용됩니다.
            df = df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

            plt.clf()

            # 박스플롯 시각화로 잘 제거되었는지 확인
            plt.figure(figsize=(12, 6))
            sns.boxplot(data=df)
            plt.xticks(rotation=45)
            st.pyplot(plt)

    elif radio_eda == "변수 간의 관계 시각화":
        radio_plot = st.radio(label="plot", label_visibility='collapsed', horizontal=True, 
                              options=["Pair Plot", "Bar", "Pie", "Histogram", "Violin Plot", "Linear, Scatter", "Corrcoef"])
        if radio_plot == "Pair Plot":
            with st.expander("Source"):
                st.code(""" 
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt
                        
sns.pairplot(df)
plt.show()
                """)
            st.image("./streamlit_images/marketing_strategy/seaborn_pairplot.png")

        elif radio_plot == "Bar":
            with st.expander("Source"):
                st.code("""
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt
                                                
g = sns.FacetGrid(df, col="Churn", height=4, aspect=1.5)
g.map(plt.hist, "Age")
plt.show()

# 총 평균 추가 요금 (Avg_additional_charges_total)
g.map(plt.hist, "Avg_additional_charges_total")
plt.show()

# 가입 기간 (Lifetime) - 사용자가 체육관에 처음 등록한 이후 경과한 시간(개월 단위).
g.map(plt.hist, "Lifetime")
plt.show()
                """)
            plt.clf()

            g = sns.FacetGrid(df, col="Churn", height=4, aspect=1.5)
            g.map(plt.hist, "Age")
            st.pyplot(plt)

            # 총 평균 추가 요금 (Avg_additional_charges_total)
            g.map(plt.hist, "Avg_additional_charges_total")
            st.pyplot(plt)

            # 가입 기간 (Lifetime) - 사용자가 체육관에 처음 등록한 이후 경과한 시간(개월 단위).
            g.map(plt.hist, "Lifetime")
            st.pyplot(plt)
        
        elif radio_plot == "Pie":
            with st.expander("Source"):
                st.code("""
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt
                        
# 이탈 분포 계산
churn_counts = df['Churn'].value_counts()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 막대 차트
axes[0].bar(churn_counts.index, churn_counts.values)
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(['Retained', 'Churned'])
axes[0].set_xlabel('Churn')
axes[0].set_ylabel('Number of Customers')
axes[0].set_title('Bar Chart')

# 원형 차트
axes[1].pie(churn_counts.values, labels=['Retained', 'Churned'], autopct='%1.1f%%', startangle=90)
axes[1].set_title('Pie Chart')

# 레이아웃 조정
fig.suptitle('Customer Churn Distribution Overview', fontsize=16)
plt.tight_layout()
plt.show()
                """)
            plt.clf()

            # Calculate churn distribution
            churn_counts = df['Churn'].value_counts()

            # Create subplots
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            # Bar Chart
            axes[0].bar(churn_counts.index, churn_counts.values)
            axes[0].set_xticks([0, 1])
            axes[0].set_xticklabels(['Retained', 'Churned'])
            axes[0].set_xlabel('Churn')
            axes[0].set_ylabel('Number of Customers')
            axes[0].set_title('Bar Chart')

            # Pie Chart
            axes[1].pie(churn_counts.values, labels=['Retained', 'Churned'], autopct='%1.1f%%', startangle=90)
            axes[1].set_title('Pie Chart')

            # Adjust layout
            fig.suptitle('Customer Churn Distribution Overview', fontsize=16)
            plt.tight_layout()
            st.pyplot(plt)

        elif radio_plot == "Histogram":
            with st.expander("Source"):
                st.code("""
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt
                        
# 나이 분포
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 히스토그램
axes[0].hist(df['Age'], bins=20)
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Age Distribution Histogram')

# 박스 플롯
axes[1].boxplot(df['Age'])
axes[1].set_xlabel('Age')
axes[1].set_title('Age Distribution Box Plot')

# 레이아웃 조정
fig.suptitle('Customer Age Distribution', fontsize=16)
plt.tight_layout()
plt.show()
                """)
            plt.clf()

            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            axes[0].hist(df['Age'], bins=20)
            axes[0].set_xlabel('Age')
            axes[0].set_ylabel('Frequency')
            axes[0].set_title('Age Distribution Histogram')

            axes[1].boxplot(df['Age'])
            axes[1].set_xlabel('Age')
            axes[1].set_title('Age Distribution Box Plot')

            fig.suptitle('Customer Age Distribution', fontsize=16)
            plt.tight_layout()
            st.pyplot(plt)
        
        elif radio_plot == "Violin Plot":
            with st.expander("Source"):
                st.code("""
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt
                        
# 계약 기간 분석

# 막대 차트: 계약 기간 빈도
contract_counts = df['Contract_period'].value_counts()

# Set color palette
sns.set_palette("Set2")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 막대 차트
axes[0].bar(contract_counts.index, contract_counts.values, color=sns.color_palette("Set2"))
axes[0].set_xlabel('Contract Period (Months)')
axes[0].set_ylabel('Number of Customers')
axes[0].set_title('Contract Period Frequency')
axes[0].grid(True, linestyle='--', alpha=0.7)

# 바이올린 플롯 with hue
# hue로 지정한 변수를 기준으로 색상을 변경하여 서로 다른 그룹을 시각화
sns.violinplot(x='Contract_period', y='Age', data=df, ax=axes[1], hue='Contract_period', palette="coolwarm", dodge=False, legend=False)
axes[1].set_xlabel('Contract Period (Months)')
axes[1].set_ylabel('Age')
axes[1].set_title('Age Distribution by Contract Period')
axes[1].grid(True, linestyle='--', alpha=0.7)

# 레이아웃 조정 및 타이틀 추가
fig.suptitle('Contract Period Analysis', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
                """)

            plt.clf()
            # Contract Period Analysis

            # Bar Chart: Contract Period Frequency
            contract_counts = df['Contract_period'].value_counts()

            # Set color palette
            sns.set_palette("Set2")

            # Create subplots
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            # Bar Chart
            axes[0].bar(contract_counts.index, contract_counts.values, color=sns.color_palette("Set2"))
            axes[0].set_xlabel('Contract Period (Months)')
            axes[0].set_ylabel('Number of Customers')
            axes[0].set_title('Contract Period Frequency')
            axes[0].grid(True, linestyle='--', alpha=0.7)

            # Violin Plot with hue
            sns.violinplot(x='Contract_period', y='Age', data=df, ax=axes[1], hue='Contract_period', palette="coolwarm", dodge=False, legend=False)
            axes[1].set_xlabel('Contract Period (Months)')
            axes[1].set_ylabel('Age')
            axes[1].set_title('Age Distribution by Contract Period')
            axes[1].grid(True, linestyle='--', alpha=0.7)

            # Adjust layout and add a main title
            fig.suptitle('Contract Period Analysis', fontsize=16)
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            st.pyplot(plt)

        elif radio_plot == "Linear, Scatter":
            with st.expander("Source"):
                st.code("""
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt
                        
# 총 평균 수업 빈도(Avg_class_frequency_total) 분석

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 선형 플롯: 가입 기간(Lifetime)의 총 평균 수업 빈도
sns.lineplot(x='Lifetime', y='Avg_class_frequency_total', data=df, ax=axes[0])
axes[0].set_xlabel('Lifetime (Months)')
axes[0].set_ylabel('Average Class Frequency')
axes[0].set_title('Average Class Frequency Over Lifetime')

# 산점도 플롯: 수업 빈도(Class Frequency) vs. 고객 이탈(Churn)
sns.scatterplot(x='Avg_class_frequency_total', y='Churn', data=df, ax=axes[1])
axes[1].set_xlabel('Average Class Frequency')
axes[1].set_ylabel('Churn')
axes[1].set_title('Class Frequency vs. Churn')

# 레이아웃 조정
fig.suptitle('Average Class Frequency Analysis', fontsize=16)
plt.tight_layout()
plt.show()
                """)
            plt.clf()

            # Average Class Frequency Analysis

            # Create subplots
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            # Line Plot: Average Class Frequency over Lifetime
            sns.lineplot(x='Lifetime', y='Avg_class_frequency_total', data=df, ax=axes[0])
            axes[0].set_xlabel('Lifetime (Months)')
            axes[0].set_ylabel('Average Class Frequency')
            axes[0].set_title('Average Class Frequency Over Lifetime')

            # Scatter Plot: Class Frequency vs. Churn
            sns.scatterplot(x='Avg_class_frequency_total', y='Churn', data=df, ax=axes[1])
            axes[1].set_xlabel('Average Class Frequency')
            axes[1].set_ylabel('Churn')
            axes[1].set_title('Class Frequency vs. Churn')

            # Adjust layout
            fig.suptitle('Average Class Frequency Analysis', fontsize=16)
            plt.tight_layout()
            st.pyplot(plt)
    
        elif radio_plot == "Corrcoef":
            with st.expander("Source"):
                st.code("""
# python jupyter notebook
import seaborn as sns
import matplotlib.pyplot as plt
                                                
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap=plt.cm.Blues, fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
                """)
            plt.clf()

            plt.figure(figsize=(10, 8))
            sns.heatmap(df.corr(), annot=True, cmap=plt.cm.Blues, fmt=".2f")
            plt.title('Correlation Heatmap')
            st.pyplot(plt)

    elif radio_eda == "변수 변환 및 생성":
        st.code("""
import pandas as pd                
# 변수 제거
df = df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
""")

with tab[1]:
    st.subheader("Predictive Model")

    st.markdown("""
회귀 모델의 정확도를 높이는 과정 
\n 단순선형 -> 다중 or 다항, 규제를 적용 -> DecisionTreeRegressor, DecisionTreeClassifier -> 모델 튜닝[하이퍼파라미터 서치, 교차 검증, 앙상블(RF:랜덤 포레스트)]
""")
    radio_model = st.radio(label="model", label_visibility='collapsed', horizontal=True, options=["선형회귀", "다중,다항 회귀", "의사결정나무", "모델 튜닝"])

    if radio_model == "선형회귀":
        col1, col2 = st.columns(2)

        with col1:
            st.code("""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
                           
df = pd.read_csv('./data/gym_churn_us.csv')
                
X = df[["Avg_class_frequency_total"]]
y = df["Avg_class_frequency_current_month"]
                    
model = LinearRegression()
model.fit(X, y)

X_new = np.array([[1], [2], [3]])
                
model.score(X, y)
model.predict(X_new)
            """)
        with col2:
            st.text("score")
            func.image_resize("linear_model_score.png", __file__, 50)
            st.text("predict")
            func.image_resize("linear_model_predict.png", __file__, 50)
            st.text("intercept, coefficient")
            func.image_resize("linear_model_intercept_coef.png", __file__, 220)

    elif radio_model == "다중,다항 회귀":
        tab_multiple = st.tabs(['다중회귀', '다항회귀', '규제(Elastic Net)', "StandardScaler"])

        with tab_multiple[0]:
            col1, col2 = st.columns(2)

            with col1:
                st.code("""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
                    
df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
                    
X = df.drop(["Churn"], axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)

model = LinearRegression()
model.fit(X_train, y_train)
                    
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))                    
coef = pd.DataFrame({"feature_names":X.columns, "coefficient":model.coef_})
                """)
            with col2:
                st.text("score")
                func.image_resize("multiple_model_score.png", __file__, 200)
                st.text("coefficient")
                func.image_resize("multiple_model_coef.png", __file__, 400)

        with tab_multiple[1]:
            col1, col2 = st.columns(2)

            with col1:
                st.code("""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
                        
df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)

X = df.drop(["Churn"], axis=1)
y = df["Churn"]

# degree = 생성할 다항식의 최대 차수를 설정합니다. 기본값은 2입니다.
# include_bias = True로 설정하면, 절편 항인 1을 포함합니다. 기본값은 True입니다.
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)  
                                  
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, random_state=42, test_size=0.3)
                        
model = LinearRegression()
model.fit(X_train, y_train)
                        
print(X.shape, X_poly.shape)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
# y절편
print(model.intercept_)
# 계수
print(model.coef_)
                """)
            with col2:
                st.text("X, X_poly shape")
                func.image_resize("polynomial_model_shape.png", __file__, 150)
                st.text("score")
                func.image_resize("polynomial_model_score.png", __file__, 200)
                st.text("rmse")
                func.image_resize("standardscaler_model_rmse.png",__file__, 50)
                st.text("intercept, coefficient")
                func.image_resize("polynomial_model_intercept_coef.png", __file__, 500)              

        with tab_multiple[2]:
            st.text("릿지(Ridge), 라쏘(Lasso), 그리고 엘라스틱넷(Elastic Net)은 모두 회귀 분석에서 사용되는 정규화 기법입니다.")
            st.text("이들은 과적합(overfitting)을 방지하고 모델의 일반화 성능을 향상시키는 데 도움을 줍니다.")

            col1, col2 = st.columns(2)
            with col1:
                st.code("""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
                        
df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)

X = df.drop(["Churn"], axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
                        
model = ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)
model.fit(X_train, y_train)
                        
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
coef = pd.DataFrame({"feature_names":X.columns, "coefficient":model.coef_})
                """)
            with col2:
                st.text("score")
                func.image_resize("elasticnet_model_score.png", __file__, 200)
                st.text("coefficient")
                func.image_resize("elasticnet_model_coef.png", __file__, 400)

        with tab_multiple[-1]:
            st.text("StandardScaler의 중요도가 높은 모델은 주로 특성의 스케일에 민감한 알고리즘입니다.\n이러한 모델들은 입력 데이터의 스케일 차이가 결과에 직접적인 영향을 미치기 때문에, 스케일링을 통해 성능을 향상시킬 수 있습니다.")
            st.text("예 : 선형 회귀, 로지스틱 회귀, K-최근접 이웃, 서포트 벡터 머신, 주성분 분석, 인공 신경망")

            col1, col2 = st.columns(2)

            with col1:
                st.code("""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
                    
X = df.drop(["Churn"], axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
                        
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)   

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)                     

model = LinearRegression()
model.fit(X_train_poly, y_train)
                    
print(model.score(X_train_poly, y_train))
print(model.score(X_test_poly, y_test))                   
# y절편
print(model.intercept_)
# 계수
print(model.coef_)
                """)
            with col2:
                st.text("score")
                func.image_resize("standardscaler_model_score.png",__file__, 200)
                st.text("rmse")
                func.image_resize("standardscaler_model_rmse.png",__file__, 50)
                st.text("intercept, coefficient")
                func.image_resize("standardscaler_model_intercept_coef.png",__file__, 500)
                
    elif radio_model == "의사결정나무":
        tab_decision = st.tabs(["의사결정나무", "RANSAC", "모델 평가"])

        with tab_decision[0]:
            st.text("의사결정나무는 비선형 모델로, 데이터의 분포에 크게 영향을 받지 않습니다. 따라서 특성의 스케일을 조정할 필요가 없지만, \n스케일링을 통해 여러 모델의 결과를 비교하고 최적화하는 데 도움을 줄 수 있습니다.")
            col1, col2 = st.columns(2)
            
            with col1:
                st.code("""
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
                
df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
                        
X = df.drop(["Churn"], axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3) 

model = DecisionTreeClassifier(random_state=42)  
model.fit(X_train, y_train)   
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
                        
model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train, y_train)
print(model2.score(X_train, y_train))
print(model2.score(X_test, y_test))                
                                                       
                """)
            with col2:
                st.text("score")
                func.image_resize("decisiontree_model_score.png", __file__, 200)
                st.text("overfitting")
                func.image_resize("decisiontree_model_score_overfitting.png", __file__, 200)

        with tab_decision[1]:
            st.text("RANSACRegressor는 Scikit-learn에서 제공하는 강건 회귀 기법으로, 데이터에 포함된 이상치(outlier)에 영향을 최소화하여 모델을 학습하는 데 사용됩니다.")
            st.text('RANSAC은 "Random Sample Consensus"의 약자로, 샘플 데이터를 무작위로 선택하여 반복적으로 모델을 학습하고 평가하여 최적의 모델을 찾습니다.')

            col1, col2 = st.columns(2)
            
            with col1:
                st.code("""
import pandas as pd
import numpy as np
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
                        
df = pd.read_csv('https://raw.githubusercontent.com/rasbt/'
                 'python-machine-learning-book-3rd-edition/'
                 'master/ch10/housing.data.txt',
                 header=None,
                 sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
              'NOX', 'RM', 'AGE', 'DIS', 'RAD',
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

X = df[['RM']].values
y = df['MEDV'].values                        

ransac = RANSACRegressor(LinearRegression(),
                         max_trials=100,
                         min_samples=50,
                         loss='absolute_error',
                         residual_threshold=5.0,
                         random_state=0)

ransac.fit(X, y)

inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

line_X = np.arange(3, 10, 1)
line_y_ransac = ransac.predict(line_X[:, np.newaxis])
plt.scatter(X[inlier_mask], y[inlier_mask],
            c='steelblue', edgecolor='white',
            marker='o', label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask],
            c='limegreen', edgecolor='white',
            marker='s', label='Outliers')
plt.plot(line_X, line_y_ransac, color='black', lw=2)
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000s [MEDV]')
plt.legend(loc='upper left')

plt.show()                        
""")
            with col2:
                st.image("./streamlit_images/marketing_strategy/ransac_plt.png", use_column_width=True)

        with tab_decision[2]:
            st.text("Receiver Operating Characteristic (ROC) 곡선은 이진 분류 모델의 성능을 평가하는 데 사용되는 그래프입니다.")

            col1, col2 = st.columns(2)

            with col1:
                st.code("""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score                     

y_pred = model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)
test_precision = precision_score(y_test, y_pred, average='binary')
test_recall = recall_score(y_test, y_pred, average='binary')
test_f1 = f1_score(y_test, y_pred, average='binary')

print(f'Test Accuracy: {test_accuracy:.4f}')
print(f'Test Precision: {test_precision:.4f}')
print(f'Test Recall: {test_recall:.4f}')
print(f'Test F1 Score: {test_f1:.4f}')
""")
                st.code("""
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
                                                                        
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix (Test Set)')
plt.show()
""")
                
                st.code("""
from sklearn.metrics import roc_curve, roc_auc_score
                        
y_pred_proba = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

roc_auc = roc_auc_score(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()                        
""")

            with col2:
                st.text("evaluation")
                func.image_resize("decisiontree_model_evaluation.png",__file__,150)
                st.text("confusion matrix")
                func.image_resize("decisiontree_model_confusion_matrix.png", __file__, 400)
                st.text("ROC Curve")
                func.image_resize("decisiontree_model_roc_curve.png",__file__,400)
                
    elif radio_model == "모델 튜닝":
        tab_tuning = st.tabs(["하이퍼파라미터 서치", "교차 검증", "랜덤 포레스트", "GridSearch + KFlod + RandomForest", "AdaBoost", "모델 비교"])

        with tab_tuning[0]:
            col1, col2 = st.columns(2)
            with col1:
                st.code("""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
X = df.drop(["Churn"], axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()

# 하이퍼파라미터 그리드 설정
param_grid = {
    # 트리의 최대 깊이. 과적합을 방지하기 위해 사용합니다.
    'max_depth': [None] + [i for i in range(1, 15 + 1)],
    # 내부 노드를 분할하기 위한 최소 샘플 수. 이 값이 높을수록 과적합을 줄일 수 있습니다.
    'min_samples_split': [i for i in range(2, 10)],
    'random_state' : [42]
}   

# 그리드 서치 설정
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy')

# 그리드 서치 실행
grid_search.fit(X_train, y_train)

# 최적의 파라미터 및 성능 확인
print("최적의 파라미터:", grid_search.best_params_)
print("최고 정확도:", grid_search.best_score_)

# 최적의 모델로 예측 수행
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# 분류 성능 보고서
# precision, recall, f1-score: 각 클래스에 대한 성능 지표.
# support: 각 클래스의 실제 샘플 수.
# accuracy: 전체 정확도.
# macro avg: 각 클래스의 평균을 단순 평균한 것.
# weighted avg: 각 클래스의 성능 지표를 샘플 수로 가중 평균한 것
print(classification_report(y_test, y_pred))                                                
""")
            with col2:
                st.text("evaluation")
                func.image_resize("gridsearch_model_evaluation_01.png",__file__, 150)
                st.text("classification_report")
                func.image_resize("gridsearch_model_evaluation_02.png",__file__, 200)
        
        with tab_tuning[1]:
            col1, col2 = st.columns(2)
            with col1:
                st.code("""
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
                        
df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
X = df.drop(["Churn"], axis=1)
y = df["Churn"]
                        
kf = KFold(n_splits=5, shuffle=True, random_state=42)

model = DecisionTreeClassifier(random_state=42)

for i, (train_index, test_index) in enumerate(kf.split(X)):
    X_train, X_test = X.iloc[train_index, :], X.iloc[test_index, :]
    y_train, y_test = y[train_index], y[test_index]
    
    # 모델 학습
    model.fit(X_train, y_train)
    
    # 예측
    y_pred = model.predict(X_test)
    
    # 정확도 계산
    print(classification_report(y_test, y_pred))                        
""")
            with col2:
                st.text("evaluation")
                func.image_resize("kfold_model_evaluation_06.png",__file__, 150)
                st.text("classification_report")
                st.image("./streamlit_images/marketing_strategy/kfold_model_evaluation_01.png", width=500)
                st.image("./streamlit_images/marketing_strategy/kfold_model_evaluation_02.png", width=500)
                st.image("./streamlit_images/marketing_strategy/kfold_model_evaluation_03.png", width=500)
                st.image("./streamlit_images/marketing_strategy/kfold_model_evaluation_04.png", width=500)
                st.image("./streamlit_images/marketing_strategy/kfold_model_evaluation_05.png", width=500)

        with tab_tuning[2]:
            col1, col2 = st.columns(2)
            with col1:
                st.code("""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier                   

df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
X = df.drop(["Churn"], axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)                        
                """)
                with st.expander("모델 평가 Source Code"):
                    st.code("""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns       
from sklearn.metrics import roc_curve, roc_auc_score                                             
                        
y_pred = model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)
test_precision = precision_score(y_test, y_pred, average='binary')
test_recall = recall_score(y_test, y_pred, average='binary')
test_f1 = f1_score(y_test, y_pred, average='binary')                                           
                    """)
                    st.code("""
print(classification_report(y_test, y_pred))
                    """)
                    st.code("""
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix (Test Set)')
plt.show()
                    """)
                    st.code("""
y_pred_proba = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

roc_auc = roc_auc_score(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()
                    """)
            with col2:
                st.text("모델 평가")
                st.text("evaluation")
                func.image_resize("randomforest_model_evaluation_01.png",__file__, 150)
                st.text("classification_report")
                func.image_resize("randomforest_model_evaluation_02.png",__file__, 200)
                st.text("confusion matrix")
                func.image_resize("randomforest_model_confusion_matrix.png",__file__, 400)
                st.text("roc curve")
                func.image_resize("randomforest_model_roc_curve.png",__file__, 400)

        with tab_tuning[3]:
            col1, col2 = st.columns(2)
            with col1:
                st.code("""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
                        
df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
X = df.drop(["Churn"], axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)    

# 하이퍼파라미터 그리드 설정
param_grid = {
    # 랜덤 포레스트에 포함할 결정 트리의 수입니다. 기본값은 100입니다. 이 값이 클수록 모델의 성능이 향상될 수 있지만, 계산 비용도 증가합니다.
    'n_estimators': [10, 50, 100],
    # 트리의 최대 깊이. 과적합을 방지하기 위해 사용합니다.
    'max_depth': [None] + [i for i in range(1, 15 + 1)],
    # 내부 노드를 분할하기 위한 최소 샘플 수. 이 값이 높을수록 과적합을 줄일 수 있습니다.
    'min_samples_split': [i for i in range(2, 10)],
    'random_state' : [42]
}      

# StratifiedKFold는 Scikit-learn에서 제공하는 교차 검증 방법 중 하나로, 데이터를 K개의 폴드로 나눌 때 각 폴드의 클래스 비율을 원본 데이터와 동일하게 유지하는 방법입니다
cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)   

grid_search = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_grid, cv=cv_strategy)  
grid_search.fit(X_train, y_train)                                                                                                         
                """)
                with st.expander("모델 평가 Source Code"):
                    st.code("""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns       
from sklearn.metrics import roc_curve, roc_auc_score                                             
                        
y_pred = model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)
test_precision = precision_score(y_test, y_pred, average='binary')
test_recall = recall_score(y_test, y_pred, average='binary')
test_f1 = f1_score(y_test, y_pred, average='binary')                                           
                    """)
                    st.code("""
print(classification_report(y_test, y_pred))
                    """)
                    st.code("""
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix (Test Set)')
plt.show()
                    """)
                    st.code("""
y_pred_proba = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

roc_auc = roc_auc_score(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()
                    """)
            with col2:
                st.text("모델 평가")
                st.text("evaluation")
                func.image_resize("grid_kfold_randomforest_model_evaluation_01.png",__file__, 150)
                st.text("classification_report")
                func.image_resize("grid_kfold_randomforest_model_evaluation_02.png",__file__, 150)
                st.text("confusion matrix")
                func.image_resize("grid_kfold_randomforest_model_confusion_matrix.png",__file__, 400)
                st.text("roc curve")
                func.image_resize("grid_kfold_randomforest_model_roc_curve.png",__file__, 400)

        with tab_tuning[4]:
            col1, col2 = st.columns(2)
            with col1:
                st.code("""
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

df = pd.read_csv('./data/gym_churn_us.csv')
df.drop(["Phone", "Near_Location"], axis=1, inplace=True)
X = df.drop(["Churn"], axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 약한 학습기로 결정 트리 사용
base_estimator = DecisionTreeClassifier(max_depth=1)      

# AdaBoost 모델 초기화
model = AdaBoostClassifier(estimator=base_estimator, n_estimators=50, random_state=42)

# 모델 학습
model.fit(X_train, y_train)                                          
                """)
                with st.expander("모델 평가 Source Code"):
                    st.code("""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns       
from sklearn.metrics import roc_curve, roc_auc_score                                             
                        
y_pred = model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)
test_precision = precision_score(y_test, y_pred, average='binary')
test_recall = recall_score(y_test, y_pred, average='binary')
test_f1 = f1_score(y_test, y_pred, average='binary')                                           
                    """)
                    st.code("""
print(classification_report(y_test, y_pred))
                    """)
                    st.code("""
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix (Test Set)')
plt.show()
                    """)
                    st.code("""
y_pred_proba = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

roc_auc = roc_auc_score(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()
                    """)
            with col2:
                st.text("모델 평가")
                st.text("evaluation")
                func.image_resize("adaboost_model_evaluation_01.png",__file__, 150)
                st.text("classification_report")
                func.image_resize("adaboost_model_evaluation_02.png",__file__, 200)
                st.text("confusion matrix")
                func.image_resize("adaboost_model_confusion_matrix.png",__file__, 400)
                st.text("roc curve")
                func.image_resize("adaboost_model_roc_curve.png",__file__, 400)

        with tab_tuning[5]:
            st.image("./streamlit_images/marketing_strategy/model_comparison.png", use_column_width=True)
            with st.expander("Source Code", expanded=False):
                st.code("""
import numpy as np
import matplotlib.pyplot as plt
                        
models = ['DecisionTree','GridSearch','KFold', 'Random Forest', 'Grid+KFold+RF', 'AdaBoost']

# accuracy, precision, recall, f1 score
decisiontree = [0.8875, 0.7819, 0.7690, 0.7754]
gridsearch = [0.8842, 0.7867, 0.7426, 0.7640]
kfold = [0.8962, 0.8341, 0.8017, 0.8176]
randomforest = [0.9108, 0.8403, 0.7987, 0.8190]
grid_kfold_randomforest = [0.9150, 0.8478, 0.8086, 0.8277]
adaboost = [0.9225, 0.8646, 0.8218, 0.8426]        

accuracy = [decisiontree[0], gridsearch[0], kfold[0], randomforest[0], grid_kfold_randomforest[0], adaboost[0]]
precision = [decisiontree[1], gridsearch[1], kfold[1], randomforest[1], grid_kfold_randomforest[1], adaboost[1]]
recall = [decisiontree[2], gridsearch[2], kfold[2], randomforest[2], grid_kfold_randomforest[2], adaboost[2]]
f1_score = [decisiontree[3], gridsearch[3], kfold[3], randomforest[3], grid_kfold_randomforest[3], adaboost[3]]

# Set the width of the bars
bar_width = 0.1

# Set the positions of the bars on the x-axis
r1 = np.arange(len(models))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]   

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(r1, accuracy, bar_width, label='Accuracy')
bars2 = ax.bar(r2, precision, bar_width, label='Precision')
bars3 = ax.bar(r3, recall, bar_width, label='Recall')
bars4 = ax.bar(r4, f1_score, bar_width, label='F1-score')

# Add labels, title, and legend
ax.set_xlabel('Models')
ax.set_ylabel('Scores')
ax.set_title('Model Comparison')
ax.set_xticks([r + bar_width for r in range(len(models))])
ax.set_xticklabels(models)
ax.legend(loc='lower center')

# Add value labels on top of bars
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(bars1)
autolabel(bars2)
autolabel(bars3)
autolabel(bars4)

# Display the chart
plt.tight_layout()
plt.show()                                                                                     
                """)
          
with tab[-1]:
    st.subheader("Marketing")

    st.markdown("회원탈퇴에는 **가입 기간**, **월 수업 빈도**, 나이 등이 가장 많은 영향이 미쳤다.")
    st.markdown("""서로 다른 두 회원 데이터셋을 사용해 탈퇴예측모델을 만들어 비교해보았더니 주요 변수로 **가입 기간(멤버십 기간)**이 공통적으로 나타났습니다. 이에 따른 마케팅 전략을 제안합니다.""")

    col1, col2 = st.columns(2)
    with col1:
        st.text("GridSearch + KFold + RandomForest Model Coefficient")
        func.image_resize("grid_kfold_randomforest_model_coef.png",__file__,500)
    with col2:
        radio_strategy = st.radio(label="strategy", label_visibility="collapsed", horizontal=True, options=["온라인", "오프라인"])    
        
        if radio_strategy == "온라인":
            st.markdown("### 온라인")
            st.markdown("""**1. 타겟 광고 캠페인**
                            \n- 가입 기간이 짧은 회원을 대상으로 특별 할인이나 혜택을 제공하는 광고를 진행합니다.
                            \n- 예: "3개월 이내 가입한 회원님께 20% 할인 제공!"과 같은 메시지를 사용할 수 있습니다.""")
            st.markdown("""**2. 리타게팅 광고**
                            \n- 탈퇴 가능성이 높은 회원에게 리타게팅 광고를 통해 재가입을 유도하는 메시지를 보냅니다.
                            \n- 가입 기간에 따라 개인화된 혜택을 제시하여 다시 방문하도록 유도합니다.""")
            st.markdown("""**3. 소셜 미디어 캠페인**
                            \n- 장기 가입 회원의 성공 사례나 혜택을 강조하는 콘텐츠를 제작하여 소셜 미디어에서 공유합니다.
                            \n- 가입 기간이 긴 회원의 후기나 경험담을 활용해 신뢰성을 높입니다.""")
            st.markdown("""**4. 이메일 마케팅**
                            \n- 특정 기간 동안 활동이 적었던 회원에게 맞춤형 이메일을 발송하여 관심을 재유도합니다.
                            \n- 예: "당신의 멤버십 기간이 6개월이 되셨습니다! 특별한 혜택을 확인하세요!"와 같은 내용.""")
            
        elif radio_strategy == "오프라인":
            st.markdown("### 오프라인")
            st.markdown("""**1. 회원 초대 이벤트**
                            \n- 가입 기간이 짧은 회원을 초대하여 무료 체험 클래스나 이벤트를 진행합니다.
                            \n- 기존 회원과의 네트워킹 기회를 제공하여 소속감을 느끼게 합니다.""")
            st.markdown("""**2. 특별 프로모션**
                            \n- 가입 기간이 짧은 회원에게 특별 할인 혜택이나 추가 서비스(예: PT 무료 체험)를 제공합니다.
                            \n- 이와 함께 멤버십 연장 혜택도 함께 제시합니다.""")
            st.markdown("""**3. 고객 피드백 수집**
                            \n- 탈퇴 가능성이 있는 회원을 대상으로 설문조사를 진행하여 이탈 이유를 파악합니다.
                            \n- 이를 통해 서비스를 개선하고 개인화된 솔루션을 제공할 수 있습니다.""")
            st.markdown("""**4. 장기 가입 유도 프로그램**
                            \n- 특정 기간 이상 가입 시 보상 프로그램을 마련하여 장기 가입을 유도합니다.
                            \n- 예: "1년 이상 가입 시 1개월 무료"와 같은 인센티브 제공.""")
            
