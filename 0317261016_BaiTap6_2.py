def credit_score(
        income,
        credit_history_year,
        has_bad_debt = False 
):
    """
    Tham số:
        - income: thu nhập hàng tháng
        - credit_history_year: số năm có lịch tín dụng
        - has_bad_debt (False): Có nợ xấu hay không
    """
    # Vòng lặp logic
    if has_bad_debt == True:
        return "Reject"
    elif income < 10000000 or credit_history_year < 1:
        return "High Rick"
    elif income >= 20000000 and credit_history_year >= 3:
        return "VIP"
    else: 
        return "Standard"

#=================
# KIỂM TRA LOGIC
#=================

vay_tin_dung = credit_score(25000000, 5, False)
print(f"Vay tín dụng ngân hàng: {vay_tin_dung}")