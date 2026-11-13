import pytest

from branch import Branch
from client import Client
from everydayaccount import EverydayAccount
from savingsaccount import SavingsAccount


@pytest.fixture
def branch():
    return Branch(1, "Adelaide branch", "Adelaide", "00001111")


@pytest.fixture
def client(branch):
    return Client(1, "John", "00000001", "2026/08/05", 20, True, branch)


@pytest.fixture
def savings():
    return SavingsAccount(101, "savings", 3000, 1, 0.03)


@pytest.fixture
def everyday():
    return EverydayAccount(102, "everyday", 8000, 1)


@pytest.fixture
def client_with_accounts(client, savings, everyday):
    client.add_account(savings)
    client.add_account(everyday)
    return client
