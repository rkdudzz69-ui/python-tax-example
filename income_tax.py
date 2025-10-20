income = 4500
tax = 0

if income >= 10000:
    level = "고소득자"
    tax = income * 0.5
elif income >= 5000:
    level = "중간소득자"
    tax = income * 0.25
else:
    level = "저소득자"
    tax = income * 0.1

print("\n===== 소득 분류 결과 =====")
print("소득 수준:", level)
print("연소득:", income, "만원")
print("예상 세금:", int(tax), "만원")
