import pytest

from branch import Branch
from client import Client
from everydayaccount import EverydayAccount
from savingsaccount import SavingsAccount
from transaction import Transaction


@pytest.mark.parametrize("field,value", [(0, True), (1, ""), (3, 0)])
def test_invalid_account_identity(field, value):
    data = [101, "everyday", 1000, 1]
    data[field] = value
    with pytest.raises(ValueError):
        EverydayAccount(*data)


@pytest.mark.parametrize("field,value", [(0, True), (1, ""), (4, -1),
                                         (5, 1), (6, "wrong branch")])
def test_invalid_client_data(field, value):
    data = [1, "John", "1234", "2026/08/05", 20, True, None]
    data[field] = value
    with pytest.raises(ValueError):
        Client(*data)


@pytest.mark.parametrize("field,value", [(0, 0), (1, " "), (4, "unknown")])
def test_invalid_branch_data(field, value):
    data = [1, "Adelaide", "Adelaide", "1234", "closed"]
    data[field] = value
    with pytest.raises(ValueError):
        Branch(*data)


@pytest.mark.parametrize("field,value", [(0, ""), (1, True), (1, -1),
                                         (2, " "), (3, "unknown")])
def test_invalid_transaction_data(field, value):
    data = ["deposit", 10, "Cash", "pending"]
    data[field] = value
    with pytest.raises(ValueError):
        Transaction(*data)


def test_linked_objects_can_be_displayed(
    client_with_accounts, branch, savings
):
    client_with_accounts.set_preferred_branch(branch)
    assert str(branch) == "Adelaide branch:1:Adelaide:00001111:closed"
    assert "John" in str(client_with_accounts)
    assert "Adelaide branch" in str(client_with_accounts)
    assert str(savings) == "101, savings, 3000, 1"
    assert repr(savings) == "SavingsAccount(account_num=101)"
    assert repr(branch) == "Branch(branch_num=1)"
    assert repr(client_with_accounts) == "Client(client_num=1)"


def test_savings_rejects_invalid_interest_and_overdraw(savings):
    with pytest.raises(ValueError):
        SavingsAccount(1, "savings", 1500, 1, -0.03)
    assert savings.withdrawal(3001) is False
    assert savings.Balance == 3000
    assert savings.TransactionCollection == []


def test_invalid_key_does_not_match_an_account(client_with_accounts):
    assert client_with_accounts.get_account(101.0) is None


def test_transaction_description_is_preserved_when_update_is_invalid():
    record = Transaction("deposit", 20, "Cash")
    record.set_description("")
    assert record.Description == "Cash"
    assert repr(record) == "Transaction('deposit', 20)"
