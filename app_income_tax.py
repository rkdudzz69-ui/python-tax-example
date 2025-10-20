import streamlit as st
from income_tax import classify_and_tax

st.set_page_config(page_title="소득 분류 & 세금 계산기", page_icon="💰")
st.title("💰 소득 분류 & 세금 계산기")
st.caption("고소득 50% · 중간소득 25% · 저소득 10% 적용")

income = st.number_input("연소득 (만원 단위)", min_value=0, step=100, value=4500)

if st.button("계산하기"):
    level, rate, tax = classify_and_tax(income)
    st.success(f"소득 수준: **{level}**")
    st.metric("적용 세율", f"{int(rate*100)}%")
    st.metric("예상 세금", f"{tax:,} 만원")
