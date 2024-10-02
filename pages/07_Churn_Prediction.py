import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

st.set_page_config(page_title="회원탈퇴예측", layout="wide")

st.title("회원탈퇴예측")

tab = st.tabs(['데이터 준비', '모델 학습', '모델 평가 및 튜닝'])

with tab[0]:
    predict_data = pd.read_csv('./database/predict_data2.csv', encoding='cp949')

    st.subheader('데이터 준비')
    st.dataframe(predict_data, use_container_width=True)
    with st.expander("Source Code"):
        st.code('''
import pandas as pd
from dateutil.relativedelta import relativedelta

customer = pd.read_csv('./database/customer_join.csv', encoding='cp949')
uselog_months = pd.read_csv('./database/use_log_months.csv', encoding='cp949')
                
uselog = pd.DataFrame()

for i in range(1, len(year_months)):
    tmp = uselog_months.loc[uselog_months["연월"]==year_months[i]]
    tmp = tmp.rename(columns={"count":"count_0"})
    tmp_before = uselog_months.loc[uselog_months["연월"]==year_months[i-1]]
    del tmp_before["연월"]
    tmp_before = tmp_before.rename(columns={"count":"count_1"})
    tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
    uselog = pd.concat([uselog, tmp], ignore_index=True)

exit_customer = customer.loc[customer["is_deleted"]==1]
exit_customer.loc[:, "exit_date"] = None
                
exit_customer.loc[:, "end_date"] = pd.to_datetime(exit_customer["end_date"])
for i in range(len(exit_customer)):
    exit_customer.iloc[i, -1] = exit_customer.iloc[i, 5] - relativedelta(months=1)

exit_customer.loc[:, "연월"] = pd.to_datetime(exit_customer.loc[:,"exit_date"]).dt.strftime("%Y%m")
uselog.loc[:, "연월"] = uselog.loc[:, "연월"].astype(str)
exit_uselog = pd.merge(uselog, exit_customer, on=["customer_id", "연월"], how="left")         
exit_uselog = exit_uselog.dropna(subset=["name"])
                
conti_customer = customer.loc[customer["is_deleted"]==0]
conti_uselog = pd.merge(uselog, conti_customer, on=["customer_id"], how="left")
conti_uselog = conti_uselog.dropna(subset=["name"])
conti_uselog = conti_uselog.sample(frac=1).reset_index(drop=True)
conti_uselog = conti_uselog.drop_duplicates(subset="customer_id")
                
predict_data = pd.concat([conti_uselog, exit_uselog],ignore_index=True)
predict_data["period"] = 0
predict_data.loc[:, "now_date"] = pd.to_datetime(predict_data.loc[:, "연월"], format="%Y%m")
predict_data.loc[:, "start_date"] = pd.to_datetime(predict_data.loc[:, "start_date"])
for i in range(len(predict_data)):
    delta = relativedelta(predict_data.iloc[i]['now_date'], predict_data.iloc[i]['start_date'])
    predict_data.iloc[i, -2] = int(delta.years*12 + delta.months)
predict_data = predict_data.dropna(subset=["count_1"])
                
target_col = ["campaign_name", "class_name", "gender", "count_1", "routine_flg", "period", "is_deleted"]
predict_data = predict_data[target_col]
predict_data = pd.get_dummies(predict_data)
                
del predict_data["campaign_name_2_일반"]
del predict_data["class_name_2_야간"]
del predict_data["gender_M"]
''')
with tab[1]:
    st.subheader('모델 학습')
    st.code('''
from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection
            
exit = predict_data.loc[predict_data["is_deleted"]==1]
conti = predict_data.loc[predict_data["is_deleted"]==0].sample(len(exit))
            
X = pd.concat([exit, conti], ignore_index=True)
y = X["is_deleted"]
del X["is_deleted"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)
            
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
results_test = pd.DataFrame({"y_test":y_test ,"y_pred":y_test_pred })
            
correct = len(results_test.loc[results_test["y_test"]==results_test["y_pred"]])
data_count = len(results_test)
score_test = correct / data_count
            
print(score_test)
''')
    st.image('./streamlit_images/python/python_decisiontree_predict.png', width=500)
with tab[2]:
    st.subheader('모델 평가 및 튜닝')
    radio = st.radio(label="", label_visibility='collapsed', options=["과적합 방지", "주요 변수 확인", '혼동 행렬(Confusion matrix)'], horizontal=True)

    if radio == '과적합 방지':
        st.image("./streamlit_images/python/python_decisiontree_score.png", width=300)
        st.code('''
from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection
            
X = pd.concat([exit, conti], ignore_index=True)
y = X["is_deleted"]
del X["is_deleted"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)
                
model = DecisionTreeClassifier(random_state=0, max_depth=5)
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
''')
        st.image("./streamlit_images/python/python_decisiontree_score2.png", width=300)
    elif radio == '주요 변수 확인':
        st.image('./streamlit_images/python/python_decisiontree_model_coef.png', width=500)
    elif radio == '혼동 행렬(Confusion matrix)':
        col1, col2 = st.columns(2)

        with col1:
            plt.clf()

            cm = np.array([[238, 33],
                           [17, 238]])
            disp = ConfusionMatrixDisplay(confusion_matrix=cm)
            disp.plot(cmap=plt.cm.Blues)
            st.pyplot(plt)
        with col2:
            st.markdown("**혼동 행렬을 이용한 모델 평가**")
            st.markdown("**Accuracy(예측률)** : (238 + 238) / (238 + 33 + 17 + 238) = :red[**0.9049429657794676**]")
            st.markdown("**Precision(정밀도)** : 238 / (238 + 17) = :red[**0.9333333333333333**]")
            st.markdown("**Sensitivity(민감도/재현율)** : 238 / (238 + 33) = :red[**0.8782287822878229**]")
            st.markdown("**F1-score** : 2 * (민감도 * 정밀도) / (민감도 + 정밀도) = :red[**0.9049429657794676**]")