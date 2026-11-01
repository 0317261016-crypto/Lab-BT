def calculate_emi(
        principal: float,
        annual_rate: float,
        months: int
)-> tuple:
    """
    Tính tổng số tiền lãi phải trả trong toàn bộ chu kì
    Tham số: 
        - principal (float): Số tiền ban đầu 
        - annual_rate (float): Lãi xuất hàng năm
        - months (int): Thời hạn của khoản vay
    Trả về:
        tuple: số tiền EMI trả mỗi tháng, tổng tiền lãi phải trả trong toàn bộ chu kì  
    """

  
    # Lãi suất tháng r
    r = annual_rate / 12

    # Công thức EMI với ngoặc đơn chuẩn
    emi = principal * (r * (1 + r) ** months) / (((1 + r) ** months) - 1)

    # Tính tổng tiền trả và tổng lãi
    total_payment = emi * months
    total_interest = total_payment - principal

    # Trả về 2 giá trị dưới dạng Tuple
    return emi, total_interest


# --- PHẦN THỰC THI (CHÚ Ý DÒNG NÀY) ---
p = 1000000000  # 1 tỷ
rate = 0.12  # 12%/năm
n = 12  # 12 tháng

# HỨNG 2 GIÁ TRỊ CÙNG LÚC BẰNG UNPACKING (Dùng dấu phẩy ở giữa)
emi_month, interest_total = calculate_emi(p, rate, n)

# IN KẾT QUẢ
print(
    f"Trả mỗi tháng: {emi_month:,.0f} VNĐ | Tổng lãi phải trả: {interest_total:,.0f} VNĐ"
)