import unittest, os
from unittest.mock import patch
from src.exceptions import WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="test.log")
    
    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    def _count_lines(self):
        with open(self.account.log_file, "r") as file:
            return len(file.readlines())
        
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es correcto")

    def test_withdraw(self):
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 500, "El balance no es correcto")

    def test_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es correcto")
        
    def test_transfer(self):
        target_account = BankAccount(balance=500)
        new_balance = self.account.transfer(500, target_account)
        assert new_balance == 500
        assert target_account.balance == 1000
        
    def test_transfer_not_enough_balance(self):
        target_account = BankAccount(balance=500)
        with self.assertRaises(ValueError):
            self.account.transfer(1500, target_account)
    
    def test_log_transaction(self):
        self.account._log_transaction("Test log")
        with open(self.account.log_file, "r") as file:
            self.assertIn("Test log", file.read())
            
    def test_count_transactions(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.transfer(100, BankAccount())
        assert self._count_lines() == 4
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(500)
        assert new_balance == 500
        
    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(500)
            
    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 19
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(500)
# py -m unittest discover -v -s tests