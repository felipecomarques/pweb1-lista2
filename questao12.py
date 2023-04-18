lista = []
tamanho = int(input("Insira o tamanho da lista: "))

for i in range(tamanho):
    numero = int(input("Insira um numero: "))
    lista.append(numero)

print("A soma dos elementos eh:", sum(lista))