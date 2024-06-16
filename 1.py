import streamlit as st  # streamlit 라이브러리 임포트
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np   # numpy 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('주식 분석')




# Markdown 문법으로 작성된 문장 출력
st.markdown(
    '''
    # 1. 주식 관련 데이터를 홈페이지에서 가져와서 시각화 해보기

    ## 데이터 출처
    - [기업공시채널 KIND](https://kind.krx.co.kr/disclosure/todaydisclosure.do?method=searchTodayDisclosureMain&marketType=0)

    '''
    )


# 데이터 분석
a1=pd.read_csv('C:/Users/손민구/Desktop/data/오늘의공시.csv',sep=',', encoding='euc-kr')
a1=a1.iloc[:,1:3]
a1= a1.dropna()
a1['시간'] = pd.to_datetime(a1['시간'], format='%H:%M')

a1['time_group'] = a1['시간'].dt.floor('10min')
company_counts = a1.groupby('time_group')['회사명'].nunique()
new_columns = ['시간그룹','회사개수']

company_counts.plot()


st.write('# 2. DataFrame 표시하기') 


# DataFrame 출력
col1, col2 = st.columns(2)

with col1:
    st.subheader('Original DataFrame')
    st.dataframe(a1)

with col2:
    st.subheader('Company Counts')
    st.dataframe(company_counts)


# 그래프 출력

st.write('# 3. 시간대별 공시를 내는 회사 개수') 
# streamlit으로 그래프 생성 및 표시
fig, ax = plt.subplots(figsize=(12, 6))
company_counts.plot(ax=ax)
ax.set_xlabel('Time')
ax.set_ylabel('Unique Companies')
st.pyplot(fig)

st.write('16~18시 사이에 공시를 내는 회사가 많다는걸 확인할 수 있음')
