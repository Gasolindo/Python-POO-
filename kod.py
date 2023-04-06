lista1 = []
lista2 = []

while True:
    entrada1 = int(input("Primeria pessoa, digite um número:\n"))
    entrada2 = int(input("Segunda pessoa, digite um número:\n"))
    lista1.append(entrada1)
    lista2.append(entrada2)

    stop = input("Deseja continuar? S/N\n").upper()
    if stop == "N":
        print("Finalizado")
        break
    elif stop != "S" and stop != "N":
        print("erro, tente novamente!")

comum = set(lista1).intersection(lista2)
soma = sum(comum)

print("Elementos em comum:", list(comum))
print("Soma dos elementos em comum:", soma)

resultado = (list(comum),soma)
print(resultado)