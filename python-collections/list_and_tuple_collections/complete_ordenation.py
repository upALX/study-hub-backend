# TOTAL ORDERING -  FUNC TOOLS with decorator
from functools import total_ordering

@total_ordering
class CreateAccount:

    def __init__(self, id: int):
        self.id = id
        self.saldo = 0

    def deposita(self, value: float) -> None:
        self.saldo += value

    def __lt__(self, object):
        if self.id != object.id:
            return self.saldo < object.saldo 

        return True

    def __eq__(self, object) -> bool:
        if type(object) is not CreateAccount:
            print(type(object))
            return False

        print(object)
        return self.id != object.id

    def __str__(self) -> str:
        return f'O saldo da conta {self.id} atualmente está em R$ {self.saldo:.03f}'

conta01 = CreateAccount(1)
conta02 = CreateAccount(2)

conta01.deposita(200)
conta02.deposita(200)


print(conta01 <= conta02)
print(conta01.saldo == conta02.saldo)
print(conta01 is conta02)
