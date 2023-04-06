class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.ligado=True

     
       
    def start(self):
        if self.ligado==False:
            self.ligado=True
            return f"carro ligado!"
        
    def stop(self):
        if self.ligado==True:
            self.ligado=False
            return f"carro desligado!"

carro = Carro("fiat","uno",2013)
if carro.start:
 print(carro.start())

if carro.stop:
    print(carro.stop())

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"{self.radius*3.14:.2f}Area total!"
    def circuferencia(self):
        return f"{2*3.14*self.radius:.2f}Circunferencia total!"
circolo=Circle(10)
print (circolo.area())
print(circolo.circuferencia())



