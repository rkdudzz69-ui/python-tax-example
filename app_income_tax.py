import streamlit as st

st.set_page_config(page_title="소득 분류 & 세금 계산기", page_icon="💰")

st.title("💰 소득 분류 & 세금 계산기")
st.caption("고소득 50% · 중간소득 25% · 저소득 10% 세율 적용")

# Streamlit은 콘솔 input() 대신 number_input 사용
income = st.number_input("연간 소득을 입력하세요 (만원 단위):", min_value=0, step=100)

if st.button("결과 보기"):
    if income >= 10000:
        level = "고소득자"
        tax = income * 0.5
    elif income >= 5000:
        level = "중간소득자"
        tax = income * 0.25
    else:
        level = "저소득자"
        tax = income * 0.1

    st.write("### 💡 결과")
    st.write("소득 수준:", level)
    st.write("연소득:", f"{income:,} 만원")
    st.write("예상 세금:", f"{int(tax):,} 만원")

