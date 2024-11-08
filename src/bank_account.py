from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction(f"Account created with balance: {balance}")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as file:
                file.write(f"{message}\n")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited: {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 8 or now.hour >= 18:
            raise WithdrawalTimeRestrictionError("You can only withdraw money between 8:00 and 18:00")
        if now.weekday() in [5, 6]:
            raise WithdrawalTimeRestrictionError("You can only withdraw money on weekdays")
        
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrawn: {amount}. New balance: {self.balance}")  
        return self.balance
    
    def transfer(self, amount, target_account):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            self._log_transaction(f"Transferred: {amount}. New balance: {self.balance}")
        else:
            self._log_transaction(f"Transfer failed: {amount}. Balance: {self.balance}")
            raise ValueError("No tienes saldo suficiente para transferir")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance: {self.balance}")
        return self.balance