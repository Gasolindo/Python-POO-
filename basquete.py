class cachorro:
    def __init__(self,tamanho,cor,peso,nome,raça):
        self.tamanho=tamanho
        self.cor=cor
        self.peso=peso
        self.nome=nome
        self.raça=raça

    def ola(self):
        print(f"Olá seu cachorro(a) se chama {self.nome},tem cor {self.cor} e a raça {self.raça}!")

    def dormir(self,dormir:str):
        print(f"{self.nome} está {self.dormir}")

    def estado(self,pular:str):
        print(f"{self.nome} está {self.pular}")


dog = cachorro(nome="pink",cor="rosa",peso=2.5,tamanho=2.0,raça="frances")

dog.ola()
dog.dormir("dormindo")
dog.estado("pulando")









    
        


