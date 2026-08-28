class BankAccount:
    def __init__(self,account, logger):
        self.account = account
        self.balance = 0
        self.logger = logger

    def deposit(self, amount):
        self.balance += amount
        self.logger.log(f"deposit {amount} kr, saldo {self.balance} kr")

    def withdraw(self, amount):
        if amount > self.balance:
            self.logger.log(f"kunde ej ta ut {amount} kr pga otillräckligt saldo,  saldo {self.balance} kr")
            return
        else:
            self.balance -= amount
            self.logger.log(f"withdraw {amount} kr, saldo {self.balance} kr")



