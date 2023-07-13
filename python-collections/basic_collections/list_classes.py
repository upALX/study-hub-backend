class CreateAccount:

    def __init__(self, id: int):
        self.id = id
        self.saldo = 0

    def deposita(self, value: float) -> None:
        self.saldo += value

    def __str__(self) -> str:
        return f'O saldo da conta {self.id} atualmente está em R$ {self.saldo:.03f}'

accountALX = CreateAccount(id=1)

accountALX.deposita(14.000)

print(accountALX)