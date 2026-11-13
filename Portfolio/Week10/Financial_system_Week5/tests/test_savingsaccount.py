def test_savings_can_reach_minimum_balance(savings):
    assert savings.withdrawal(2000)
    assert savings.Balance == 1000
    assert savings.transaction_count() == 1


def test_savings_cannot_go_below_minimum_balance(savings):
    assert savings.withdrawal(2001) is False
    assert savings.Balance == 3000
    assert savings.TransactionCollection == []
