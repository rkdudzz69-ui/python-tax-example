# 콘솔 input() 대신 재사용 가능한 함수로 분리
def classify_and_tax(income: int):
    if income >= 10000:
        level = "고소득자"; rate = 0.5
    elif income >= 5000:
        level = "중간소득자"; rate = 0.25
    else:
        level = "저소득자"; rate = 0.1
    tax = int(income * rate)
    return level, rate, tax

# (선택) 로컬에서 콘솔 테스트용
if __name__ == "__main__":
    income = int(input("당신의 연간 소득을 입력하세요 (만원 단위): "))
    level, rate, tax = classify_and_tax(income)
    print("\n===== 소득 분류 결과 =====")
    print("소득 수준:", level)
    print("연소득:", income, "만원")
    print("예상 세금:", tax, "만원")

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
