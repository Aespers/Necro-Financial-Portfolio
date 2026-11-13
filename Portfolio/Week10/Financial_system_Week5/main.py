from branch import Branch
from client import Client
from everydayaccount import EverydayAccount
from savingsaccount import SavingsAccount


def main() -> None:
    """Demonstrate client, account and transaction interactions."""
    branch = Branch(1, "Adelaide branch", "Adelaide", "00001111")
    client = Client(1, "John", "00000001", "2026/08/05", 20, True, branch)
    savings = SavingsAccount(101, "savings", 1800, 1, 0.03)
    everyday = EverydayAccount(102, "everyday", 11000, 1)
    client.add_account(savings)
    client.add_account(everyday)

    account = client.get_account(101)
    assert account is savings
    assert client.get_account(102) is everyday
    deposited = account.deposit(200)
    assert deposited
    savings_paid = account.withdrawal(1000)
    assert savings_paid
    everyday_paid = everyday.withdrawal(5000)
    assert everyday_paid

    # Both accounts reject a withdrawal, for different reasons.
    for number, amount in ((101, 1), (102, 5001)):
        selected = client.get_account(number)
        old_balance = selected.Balance
        old_count = selected.transaction_count()
        paid = selected.withdrawal(amount)
        assert not paid
        assert selected.Balance == old_balance
        assert selected.transaction_count() == old_count

    history = account.TransactionCollection
    assert [(item.Type, item.Amount) for item in history] == [
        ("deposit", 200), ("withdrawal", 1000)
    ]
    assert all(item.Status == "Processed" for item in history)
    # Clear the copy to check that the account keeps its records.
    history.clear()
    assert account.transaction_count() == 2
    print(account)
    for transaction in account.TransactionCollection:
        print(transaction)

    missing_account = client.get_account(999)
    assert missing_account is None
    deposited_after_error = account.deposit(10)
    assert deposited_after_error
    assert account.Balance == 1010
    print("The valid deposit after the failed operations was recorded.")


if __name__ == "__main__":
    main()
