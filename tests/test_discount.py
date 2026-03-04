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


@pytest.mark.parametrize("ori_price, discount_percent, err_type",[
    (-100, 10, ValueError),
    (200, 105, ValueError),
],ids=["Negative_price", "Over 100 percent discount"])

def test_discount_fail(ori_price, discount_percent, err_type):
    with pytest.raises(err_type):
        calculate_discount(ori_price, discount_percent)