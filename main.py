import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')

import pandas as pd
import plotly.express as px
import streamlit as st

# 제목
st.title("데이터 시각화 웹앱")

# 1. 데이터 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

# 2. 데이터 확인
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 3. Plotly 시각화
st.subheader("Plotly 그래프")
# 예시: x축은 첫 번째 컬럼, y축은 두 번째 컬럼으로 설정
columns = df.columns.tolist()

if len(columns) >= 2:
    fig = px.line(df, x=columns[0], y=columns[1], title=f"{columns[0]} vs {columns[1]}")
    st.plotly_chart(fig)
else:
    st.warning("데이터에 컬럼이 부족합니다.")
