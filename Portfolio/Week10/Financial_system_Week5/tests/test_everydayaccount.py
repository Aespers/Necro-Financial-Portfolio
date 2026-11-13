def test_everyday_limit_can_be_reached(everyday):
    assert everyday.withdrawal(5000)
    assert everyday.Balance == 3000
    assert everyday.transaction_count() == 1


def test_everyday_limit_is_checked_even_with_enough_money(everyday):
    assert everyday.withdrawal(5001) is False
    assert everyday.Balance == 8000
    assert everyday.TransactionCollection == []
