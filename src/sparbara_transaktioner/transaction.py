from src.sparbara_transaktioner import logger


class Transaction:
    def transfer(self, amount, from_account, to_account):
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
