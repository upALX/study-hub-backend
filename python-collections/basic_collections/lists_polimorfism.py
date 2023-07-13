class CreateAccount:

    def __init__(self, id: int):
        self.id = id
        self.saldo = 0

    def deposita(self, value: float) -> None:
        self.saldo += value

    def __str__(self) -> str:
        return f'O saldo da conta {self.id} atualmente está em R$ {self.saldo:.03f}'

class CorrenteAccount(CreateAccount):

    def pass_month(self):
        print(self.saldo)
        self.saldo -= 2
        print(self.saldo)

class PoupancaAccount(CreateAccount):

    def pass_month(self):
        self.saldo *=1.04
        print(self.saldo)
        self.saldo -= 2

conta15 = CorrenteAccount(id=900)
conta15.deposita(value=2000)
conta16 = PoupancaAccount(id=901)
conta16.deposita(value=5000)

accounts = [conta16, conta15]

for account in accounts:
    account.pass_month()
    print(account)