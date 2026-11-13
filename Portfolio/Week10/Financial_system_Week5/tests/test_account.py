import pytest

from account import Account
from everydayaccount import EverydayAccount


def test_base_account_cannot_be_created():
    with pytest.raises(TypeError):
        Account(1, "general", 1000, 1)


@pytest.mark.parametrize("amount", [True, 0, -10, float("nan"), "5"])
def test_bad_deposit_leaves_account_unchanged(everyday, amount):
    assert everyday.deposit(amount) is False
    assert everyday.Balance == 8000
    assert everyday.transaction_count() == 0


@pytest.mark.parametrize("amount", [False, -1, float("inf"), 8001])
def test_bad_withdrawal_leaves_account_unchanged(everyday, amount):
    assert everyday.withdrawal(amount) is False
    assert everyday.Balance == 8000
    assert everyday.TransactionCollection == []


def test_recorded_transactions_are_in_order_and_list_is_private(savings):
    assert savings.deposit(200)
    assert savings.withdrawal(100)
    records = savings.TransactionCollection
    assert [(record.Type, record.Amount) for record in records] == [
        ("deposit", 200), ("withdrawal", 100)
    ]
    assert all(record.Status == "Processed" for record in records)
    assert savings.Balance == 3100
    records.clear()
    assert savings.transaction_count() == 2


@pytest.mark.parametrize("balance", [-1, True, float("nan")])
def test_invalid_opening_balance(balance):
    with pytest.raises(ValueError):
        EverydayAccount(1, "everyday", balance, 1)
