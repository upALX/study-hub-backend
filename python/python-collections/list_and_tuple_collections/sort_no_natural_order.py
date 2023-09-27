# SORT BY ATTRIBUTE

class CreateAccount:

    def __init__(self, id: int):
        self.id = id
        self._saldo = 0

    def deposita(self, value: float) -> None:
        self._saldo += value

    def __lt__(self, object) -> bool: 
        return self._saldo < object._saldo

    def __eq__(self, object) -> bool:
        if type(object) is not CreateAccount:
            print(type(object))
            return False

        print(object)
        return self.id != object.id

    def __str__(self) -> str:
        return f'O saldo da conta {self.id} atualmente está em R$ {self._saldo:.03f}'


conta01 = CreateAccount(id=1)
conta01.deposita(value=10000)
conta02 = CreateAccount(id=2)
conta02.deposita(value=20000)
conta03 = CreateAccount(id=3)
conta03.deposita(value=30000)

accounts = [conta01, conta02, conta03]

from operator import attrgetter

for account in sorted(accounts, key=attrgetter("_saldo")):
    print(account)
# for account in accounts:
    
# print(accounts)

# USING NATURAL ORDER WITH POO apling __lt__ lassthan on class

for account in sorted(accounts):
    print(account)

