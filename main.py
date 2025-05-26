import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("나의 첫 Streamlit 앱")
st.write("안녕하세요!")

st.title("데이터 시각화 웹앱")

# 1. 데이터 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
try:
    df = pd.read_csv(url)
except Exception as e:
    st.error(f"데이터를 불러오는 중 오류 발생: {e}")
    st.stop()

# 2. 데이터 확인
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 3. Plotly 시각화
st.subheader("Plotly 그래프")
columns = df.columns.tolist()

if len(columns) >= 2:
    try:
        fig = px.line(df, x=columns[0], y=columns[1], title=f"{columns[0]} vs {columns[1]}")
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"그래프 그리는 중 오류 발생: {e}")
else:
    st.warning("데이터에 컬럼이 부족합니다.")
