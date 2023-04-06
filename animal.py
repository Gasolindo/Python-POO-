        
class Animal:
    def __init__(self,nome,especie):
        self.nome=nome
        self.especie=especie
    def eat(self):
        return "estou comendo" 
animal=Animal("pedro","rasta")

print(animal.eat())

class Pessoa:
    def __init__(self,nome,idade,endereço):
        self.nome=nome
        self.idade=idade
        self.endereço=endereço
    def introdutor(self):
        return f"Olá meu nome é {self.nome} e moro em {self.endereço} !"
pessoa=Pessoa("Bruno",22,"Mata-black")
print(pessoa.introdutor())
        

