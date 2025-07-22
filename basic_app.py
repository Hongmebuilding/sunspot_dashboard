import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# 페이지 제목
st.set_page_config(layout="wide")
st.title("🌞 태양흑점 데이터 분석 대시보드")
st.markdown("전체 태양흑점 데이터를 정적인 시각화로 보여줍니다.")

# 데이터 불러오기 함수
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = ["YEAR", "SUNACTIVITY"]
    df["YEAR_INT"] = df["YEAR"].astype(int)
    df["DATE"] = pd.to_datetime(df["YEAR_INT"].astype(str), format="%Y")
    df.set_index("DATE", inplace=True)
    return df

# 시각화 함수
def plot_advanced_sunspot_visualizations(df, sunactivity_col="SUNACTIVITY"):
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle("Sunspots Data Advanced Visualization", fontsize=18)

    # (a) 전체 시계열 라인 차트
    axs[0, 0].plot(df["YEAR"], df[sunactivity_col], color="blue")
    axs[0, 0].set_title("Sunspot Activity Over Time")
    axs[0, 0].set_xlabel("Year")
    axs[0, 0].set_ylabel("Sunspot Count")
    axs[0, 0].grid(True)

    # (b) 히스토그램 + KDE
    data = df[sunactivity_col].dropna()
    xs = np.linspace(data.min(), data.max(), 200)
    density = gaussian_kde(data)
    axs[0, 1].hist(data, bins=30, density=True, alpha=0.6, color="gray", label="Histogram")
    axs[0, 1].plot(xs, density(xs), color="red", linewidth=2, label="Density")
    axs[0, 1].set_title("Distribution of Sunspot Activity")
    axs[0, 1].set_xlabel("Sunspot Count")
    axs[0, 1].set_ylabel("Density")
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # (c) 상자 그림 (1900~2000)
    df_20th = df[(df["YEAR"] >= 1900) & (df["YEAR"] <= 2000)]
    axs[1, 0].boxplot(df_20th[sunactivity_col], vert=False)
    axs[1, 0].set_title("Boxplot of Sunspot Activity (1900-2000)")
    axs[1, 0].set_xlabel("Sunspot Count")

    # (d) 산점도 + 회귀선
    years = df["YEAR"].values
    y = df[sunactivity_col].values
    mask = ~np.isnan(y)
    years = years[mask]
    y = y[mask]
    axs[1, 1].scatter(years, y, s=10, alpha=0.5, label="Data Points")
    coef = np.polyfit(years, y, 1)
    axs[1, 1].plot(years, np.poly1d(coef)(years), color="red", linewidth=2, label="Trend Line")
    axs[1, 1].set_title("Trend of Sunspot Activity")
    axs[1, 1].set_xlabel("Year")
    axs[1, 1].set_ylabel("Sunspot Count")
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig

# 앱 실행
try:
    df = load_data("data/sunspots.csv")

    if not df.empty:
        st.subheader("태양흑점 데이터 종합 시각화")
        fig = plot_advanced_sunspot_visualizations(df)
        st.pyplot(fig)
    else:
        st.warning("데이터가 없습니다.")

except Exception as e:
    st.error(f"오류 발생: {e}")
    st.info("data/sunspots.csv 파일이 존재하고 YEAR 및 SUNACTIVITY 컬럼이 있어야 합니다.")
