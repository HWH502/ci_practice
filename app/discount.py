def calculate_discount(price: float, discount_percent: float) -> float:
    """
    計算折扣後價格

    price: 原價
    discount_percent: 折扣百分比（例如 20 代表 20%）
    """

    if price < 0:
        raise ValueError("Price cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percent must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    return round(price - discount_amount)