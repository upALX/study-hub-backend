class CreateAccount:

    def __init__(self, id: int):
        self.id = id
        self.saldo = 0

    def deposita(self, value: float) -> None:
        self.saldo += value

    def __eq__(self, object) -> bool:
        if type(object) is not CreateAccount:
            print(type(object))
            return False

        print(object)
        return self.id != object.id

    def __str__(self) -> str:
        return f'O saldo da conta {self.id} atualmente está em R$ {self.saldo:.03f}'

conta01 = CreateAccount(15)
conta02 = CreateAccount(16)

print(conta02 == conta01)
print(id(conta01))
print(id(conta02))
