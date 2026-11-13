from everydayaccount import EverydayAccount


def test_client_retrieves_accounts_by_number(
    client_with_accounts, savings, everyday
):
    assert client_with_accounts.get_account(101) is savings
    assert client_with_accounts.get_account(102) is everyday
    assert client_with_accounts.get_account(999) is None


def test_invalid_accounts_do_not_replace_existing_account(
    client_with_accounts, everyday
):
    client_with_accounts.add_account("not an account")
    client_with_accounts.add_account(EverydayAccount(102, "other", 0, 1))
    client_with_accounts.add_account(EverydayAccount(103, "other", 0, 2))
    assert client_with_accounts.get_account(102) is everyday
    assert client_with_accounts.get_account(103) is None


def test_accounts_with_different_rules_share_the_same_operation(
    client_with_accounts
):
    accounts = [client_with_accounts.get_account(n) for n in (101, 102)]
    assert [account.withdrawal(2500) for account in accounts] == [
        False, True
    ]
    assert [account.Balance for account in accounts] == [3000, 5500]
    assert [account.transaction_count() for account in accounts] == [0, 1]


def test_contact_and_preferred_branch_stay_valid(client, branch):
    client.set_contact("12345")
    client.set_contact("")
    client.set_preferred_branch(None)
    assert client.Contact.endswith("12345")
    assert client.PreferredBranch is branch
