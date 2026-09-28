import pytest
from bank import BankAccount


@pytest.fixture
def empty_account():
    return BankAccount()


def test_empty_account_balance(empty_account):
    assert empty_account.balance == 0


def test_deposit_into_empty_account(empty_account):
    empty_account.deposit(100)
    assert empty_account.balance == 100
