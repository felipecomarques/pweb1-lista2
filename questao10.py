lista = []
tamanho = int(input("Insira o tamanho da lista: "))

for i in range(tamanho):
    numero = int(input("Insira um numero: "))
    lista.append(numero)

print("Os numeros pares da lista sao: ")
for i in lista:
    if i % 2 == 0:
        print(i, end = " ")