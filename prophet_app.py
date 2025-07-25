# --------------------------------------------------
# [4] 시각화한 내용을 Steamlit에 배포하세요.
# 위에서 생성한 sunspots_for_prophet.csv를 다운로드 받아, 루트/data 아래에 넣어주세요.
# --------------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# 페이지 설정
st.set_page_config(page_title="🌞 Sunspot Forecast", layout="wide")
st.title("🌞 Prophet Forecast with Preprocessed Sunspot Data")

# ----------------------------------
# [1] 데이터 불러오기
# ----------------------------------
df = pd.read_csv("data/sunspots_for_prophet.csv")
df["ds"] = pd.to_datetime(df["ds"])  # datetime 변환

st.subheader("📄 데이터 미리보기")
st.dataframe(df.head())

# ----------------------------------
# [2] Prophet 모델 정의 및 학습
# ----------------------------------
# TODO: Prophet 모델을 생성하고, 11년 주기 커스텀 seasonality를 추가한 후 학습하세요.
model = Prophet(yearly_seasonality=False)
model.add_seasonality(name="sunspot_cycle", period=11, fourier_order=5)
model.fit(df)

# ----------------------------------
# [3] 예측 수행
# ----------------------------------
# TODO: 30년간 연 단위 예측을 수행하고, 결과를 forecast에 저장하세요.
future = model.make_future_dataframe(periods=30, freq="Y")
forecast = model.predict(future)

# ----------------------------------
# [4] 기본 시각화
# ----------------------------------
# TODO: model.plot()을 사용하여 예측 결과를 시각화하세요.
st.subheader("📈 Prophet Forecast Plot")
fig1 = model.plot(forecast)
st.pyplot(fig1)

st.subheader("📊 Forecast Components")
# TODO: model.plot_components()를 사용하여 구성요소를 시각화하세요.
fig2 = model.plot_components(forecast)
st.pyplot(fig2)

# ----------------------------------
# [5] 커스텀 시각화: 실제값 vs 예측값 + 신뢰구간
# ----------------------------------
st.subheader("📉 Custom Plot: Actual vs Predicted with Prediction Intervals")

# TODO: 실제값, 예측값, 신뢰구간을 하나의 plot에 시각화하세요.
fig3, ax = plt.subplots(figsize=(14, 6))

'''코드를 작성하시오'''
ax.plot(df["ds"], df["y"], label="Actual", color="black")
ax.plot(forecast["ds"], forecast["yhat"], label="Predicted", color="blue")
ax.fill_between(
    forecast["ds"].values,
    forecast["yhat_lower"].values,
    forecast["yhat_upper"].values,
    color="skyblue",
    alpha=0.4,
    label="Confidence Interval"
)
ax.set_title("Sunspots: Actual vs. Predicted with Prediction Intervals")
ax.set_xlabel("Year")
ax.set_ylabel("Sun Activity")
ax.legend()
ax.grid(True)
st.pyplot(fig3)

# ----------------------------------
# [6] 잔차 분석 시각화
# ----------------------------------
st.subheader("📉 Residual Analysis (예측 오차 분석)")

# TODO: df와 forecast를 'ds' 기준으로 병합하여 residual 컬럼을 생성하세요.
merged = pd.merge(df, forecast[["ds", "yhat"]], on="ds", how="left")
merged["residual"] = merged["y"] - merged["yhat"]

# TODO: residual 시계열을 시각화하세요.
fig4, ax2 = plt.subplots(figsize=(14, 4))

'''코드를 작성하시오'''
ax2.plot(merged["ds"], merged["residual"], label="Residual", color="purple")
ax2.axhline(0, linestyle="--", color="gray")
ax2.set_title("Residual Over Time")
ax2.set_xlabel("Year")
ax2.set_ylabel("Residual")
ax2.legend()
ax2.grid(True)
st.pyplot(fig4)

st.pyplot(fig4)

# ----------------------------------
# [7] 잔차 통계 요약 출력
# ----------------------------------
st.subheader("📌 Residual Summary Statistics")
# TODO: merged["residual"].describe()를 출력하세요.
st.write(merged["residual"].describe())
