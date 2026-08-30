import pytest

from src.sparbara_transaktioner import transaction
from src.sparbara_transaktioner.bankaccount import *
from src.sparbara_transaktioner.logger import *
from src.sparbara_transaktioner.transaction import *






@pytest.mark.integration
def test_deposit_to_account(mocker):
    logger = Logger()
    account = BankAccount("123", logger)

    spy = mocker.spy(logger, "log")

    account.deposit(500)

    assert account.balance == 500
    spy.assert_called_once_with(f"deposit {500} kr, saldo {account.balance} kr")


@pytest.mark.integration
def test_withdraw_successfully(mocker):
    logger = Logger()
    account = BankAccount("123", logger)
    account.balance = 500

    spy = mocker.spy(logger, "log")

    account.withdraw(500)

    assert account.balance == 0
    spy.assert_called_once_with("withdraw 500 kr, saldo 0 kr")

@pytest.mark.integration
def test_withdraw_failure(mocker):
    logger = Logger()
    account = BankAccount("123", logger)

    spy = mocker.spy(logger, "log")

    account.withdraw(500)
    assert account.balance == 0
    spy.assert_called_once_with("kunde ej ta ut 500 kr pga otillräckligt saldo,  saldo 0 kr")


@pytest.mark.integration
def test_send_money_between_accounts_successfully(mocker):
    logger = Logger()
    transaction = Transaction()
    account1 = BankAccount("123", logger)
    account1.balance = 500
    account2 = BankAccount("123", logger)
    account2.balance = 100

    spy = mocker.spy(logger, "log")

    transaction.transfer(500, account1, account2)

    assert account1.balance == 0
    assert account2.balance == 600
    assert spy.call_count == 2

    assert spy.call_args_list[0].args[0] == "withdraw 500 kr, saldo 0 kr"
    assert spy.call_args_list[1].args[0] == "deposit 500 kr, saldo 600 kr"


@pytest.mark.integration
def test_send_money_between_accounts_fail(mocker):
    logger = Logger()
    transaction = Transaction()
    account1 = BankAccount("123", logger)
    account1.balance = 200
    account2 = BankAccount("123", logger)
    account2.balance = 100

    spy = mocker.spy(logger, "log")

    transaction.transfer(500, account1, account2)

    assert account1.balance == 200
    assert account2.balance == 100




