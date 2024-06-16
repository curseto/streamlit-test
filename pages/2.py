import streamlit as st  # streamlit 라이브러리 임포트
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np   # numpy 라이브러리 임포트

st.title('주식 분석')

st.markdown(
    '''
    # 1. 앞으로 분석해볼 데이터들

    ## 데이터 출처
    - [기업공시채널 KIND](https://kind.krx.co.kr/disclosure/todaydisclosure.do?method=searchTodayDisclosureMain&marketType=0)
    - [38커뮤니케이션](https://www.38.co.kr/html/fund/?o=nw)
    - [DART](https://dart.fss.or.kr/dsac001/mainAll.do?selectDate=&sort=&series=&mdayCnt=2)
    - [특징주모음](https://cafe.naver.com/ca-fe/cafes/29798500/members/dT13403RZ-ERPYhWwNk69A)
    '''
    )


a1=pd.read_csv('C:/Users/손민구/Desktop/data/특징주DB.csv',sep=',')

st.markdown(' ## 2019년~2024년 급둥주 데이터 모음')
st.dataframe(a1)
