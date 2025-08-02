
https://leesumin2.streamlit.app/ | 
https://leesumin3.streamlit.app/ |
https://leesumin5.streamlit.app/

# 🌞 Sunspot Activity Analysis Dashboard

이 프로젝트는 태양흑점(Sunspot) 데이터를 기반으로 시계열 시각화와 예측을 수행하는 **데이터 분석 및 머신러닝 기반 대시보드**입니다. `Streamlit`을 활용해 웹 애플리케이션 형태로 구현되었으며, 시각적 탐색과 예측 결과를 직관적으로 확인할 수 있습니다.

---

## 📊 주요 기능

- 태양흑점 데이터에 대한 다양한 통계적 시각화
- KDE(커널 밀도 추정), 히스토그램, 박스플롯, 산점도, 회귀선 등 시각 분석
- 연도 범위, 회귀차수 등 사용자 인터랙션 기반 파라미터 조절
- Prophet 기반 시계열 예측 (11년 주기 seasonality 반영)
- 예측 결과와 실제 관측값의 비교 및 잔차 분석 시각화

---

## 🧠 ML/DL 관점의 학습 내용

| 기술 | 설명 |
|------|------|
| **Exploratory Data Analysis (EDA)** | 시계열 라인 차트, KDE, 박스플롯, 산점도 및 다항 회귀선을 통해 데이터의 분포 및 변화 추세를 시각적으로 분석함 |
| **시계열 예측 (Time Series Forecasting)** | Facebook Prophet 라이브러리를 활용해 연 단위 예측을 수행하고, 태양흑점의 11년 주기를 반영한 커스텀 seasonality 구성 |
| **선형/다항 회귀 분석** | `numpy.polyfit`으로 추세선(1차~5차 다항식)을 생성하여 장기적인 변화 경향 분석 |
| **확률 밀도 추정 (KDE)** | `scipy.stats.gaussian_kde`를 사용하여 태양흑점 활동의 분포를 추정하고 히스토그램과 함께 시각화 |
| **잔차 분석 (Residual Analysis)** | 예측값과 실제값의 차이를 시계열로 시각화하고 기술통계로 오차 패턴을 해석함 |

---
