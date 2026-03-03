import pytest
from app.discount import calculate_discount

@pytest.mark.parametrize("ori_price, discount_percent, final_price",[
    (100, 10, 90),
    (200, 20, 160),
    (50, 25, 38),
    (50, 35, 32)

])
def test_discount_normal(ori_price, discount_percent, final_price):
    cal_price = calculate_discount(ori_price, discount_percent)

    assert final_price == cal_price