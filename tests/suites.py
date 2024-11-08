import unittest
from tests.test_bank_account import TestBankAccount

def bank_account_suite():
    suite = unittest.TestSuite()
    tests = [
        "test_deposit",
        "test_withdraw",
        "test_balance",
        "test_transfer",
        "test_transfer_not_enough_balance",
        "test_log_transaction",
        "test_count_transactions"
    ]
    for test in tests:
        suite.addTest(TestBankAccount(test))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())