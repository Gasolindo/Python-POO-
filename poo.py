
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def add_account(self, conta):
        self.contas.append(conta)
        print("Conta adicionada com sucesso!")

    def remove_account(self, conta):
        if conta in self.contas:
            self.contas.remove(conta)
            print("Conta removida com sucesso!")
        else:
            print("Conta não encontrada!")

banco=Banco("jesus")
print(banco.add_account("jesus"))
print(banco.remove_account("jesus"))




        
