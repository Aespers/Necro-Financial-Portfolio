import pytest

from account_not_found_error import AccountNotFoundError
from invalid_amount_error import InvalidAmountError
from withdrawal_error import WithdrawalError


def test_withdrawal_validation_reports_balance(everyday):
    with pytest.raises(WithdrawalError, match="8000"):
        everyday.valid_withdrawal(8001)
    assert everyday.Balance == 8000
    assert everyday.transaction_count() == 0


def test_withdrawal_validation_reports_invalid_amount(savings):
    with pytest.raises(InvalidAmountError, match="positive number"):
        savings.valid_withdrawal(True)
    assert savings.Balance == 3000


def test_account_lookup_reports_missing_account(client_with_accounts):
    with pytest.raises(AccountNotFoundError, match="999"):
        client_with_accounts.require_account(999)
    assert client_with_accounts.get_account(101).AccountNum == 101
