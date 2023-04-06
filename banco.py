class BankAccout:
    def __init__ (self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,valor):
        self.valor=valor
        self.balance += valor
        return f"add o valor {valor}, saldo = {self.balance} !"
    def retire (self,saida):
        self.saida=saida
        if self.balance < saida:
            return "Saldo insuficiente para efetuar a retirada."
        else:
            self.balance > saida
            return f"Retirada de {saida} efetuada com sucesso. Novo saldo: {self.balance - saida}"
        
bankaccout=BankAccout(71,0)
print(bankaccout.deposit(100))
print(bankaccout.retire(10))