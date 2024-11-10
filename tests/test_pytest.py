import pytest
from src.bank_account import BankAccount

@pytest.mark.parametrize("amount, expected", [(500, 1500), (300, 1300), (100, 1100)])
def test_deposit_varios_ammounts(amount, expected):
    account = BankAccount(balance=1000, log_file="test.log")
    new_balance = account.deposit(amount)
    assert new_balance == expected