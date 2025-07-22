import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Streamlit 화면 설정
st.set_page_config(layout="wide")
st.title("🌞 태양흑점 데이터 분석 대시보드")
st.markdown("이 대시보드는 태양흑점 데이터를 다양한 시각화 방법으로 보여줍니다.")

# 데이터 불러오기
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = ["YEAR", "SUNACTIVITY"]
    df["YEAR_INT"] = df["YEAR"].astype(int)
    df["DATE"] = pd.to_datetime(df["YEAR_INT"].astype(str), format="%Y")
    df.set_index("DATE", inplace=True)
    return df

# 시각화 함수
def plot_advanced_sunspot_visualizations(df, bins=30, alpha=0.5, dot_size=20, poly_deg=1):
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle("Sunspots Data Advanced Visualization", fontsize=18)

    # (a) 시계열 라인 차트
    axs[0, 0].plot(df["YEAR"], df["SUNACTIVITY"], color="blue")
    axs[0, 0].set_title("Sunspot Activity Over Time")
    axs[0, 0].set_xlabel("Year")
    axs[0, 0].set_ylabel("Sunspot Count")

    # (b) 히스토그램 + KDE
    data = df["SUNACTIVITY"].dropna()
    xs = np.linspace(data.min(), data.max(), 200)
    density = gaussian_kde(data)
    axs[0, 1].hist(data, bins=bins, density=True, alpha=0.6, color="gray", label="Histogram")
    axs[0, 1].plot(xs, density(xs), color="red", linewidth=2, label="Density")
    axs[0, 1].set_title("Distribution of Sunspot Activity")
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # (c) 상자그림 (1900~2000)
    df_20th = df[(df["YEAR"] >= 1900) & (df["YEAR"] <= 2000)]
    axs[1, 0].boxplot(df_20th["SUNACTIVITY"], vert=False)
    axs[1, 0].set_title("Boxplot of Sunspot Activity (1900-2000)")
    axs[1, 0].set_xlabel("Sunspot Count")

    # (d) 산점도 + 회귀선
    years = df["YEAR"].values
    y = df["SUNACTIVITY"].values
    mask = ~np.isnan(y)
    years = years[mask]
    y = y[mask]
    axs[1, 1].scatter(years, y, s=dot_size, alpha=alpha, label="Data Points")
    coef = np.polyfit(years, y, poly_deg)
    axs[1, 1].plot(years, np.poly1d(coef)(years), color="red", linewidth=2, label="Trend Line")
    axs[1, 1].set_title("Trend of Sunspot Activity")
    axs[1, 1].set_xlabel("Year")
    axs[1, 1].set_ylabel("Sunspot Count")
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig

# 데이터 로드
df = load_data("data/sunspots.csv")

# 사이드바 파라미터
st.sidebar.title("시각화 파라미터 조절")
year_range = st.sidebar.slider("연도 범위 선택", 1700, 2020, (1750, 2000))
bins = st.sidebar.slider("히스토그램 구간 수", 5, 100, 30)
reg_degree = st.sidebar.slider("추세선 차수", 1, 5, 1)
dot_size = st.sidebar.slider("산점도 점 크기", 5, 50, 20)
dot_alpha = st.sidebar.slider("산점도 투명도", 0.1, 1.0, 0.5)

# 필터링된 데이터
df_filtered = df[(df["YEAR"] >= year_range[0]) & (df["YEAR"] <= year_range[1])]

# 시각화 출력
if not df_filtered.empty:
    st.subheader("태양흑점 데이터 종합 시각화")
    fig = plot_advanced_sunspot_visualizations(df_filtered, bins, dot_alpha, dot_size, reg_degree)
    st.pyplot(fig)
else:
    st.warning("선택한 기간에 데이터가 없습니다.")
