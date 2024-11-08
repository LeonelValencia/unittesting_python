import unittest, os
from src.user import User
from src.bank_account import BankAccount
from faker import Faker

class UserTests(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale='es_ES')
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)
        
    def test_user_with_multiple_accounts(self):
        for _ in range(3):
            account = BankAccount(
                balance=self.faker.random_int(min=1000, max=10000, step=500),
                log_file=self.faker.file_name(extension='log')
            )
            self.user.add_account(account)
            
        expected_total_balance = self.user.get_total_balance()
        total_balance = sum([account.get_balance() for account in self.user.accounts])
        self.assertEqual(expected_total_balance, total_balance)
        
    def tearDown(self) -> None:
        for account in self.user.accounts:
            if account.log_file:
                os.remove(account.log_file)