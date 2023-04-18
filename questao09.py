lista = []
tamanho = int(input("Insira o tamanho da lista: "))

for i in range(tamanho):
    numero = int(input("Insira um numero: "))
    lista.append(numero)

media = sum(lista)/tamanho
print("A media eh:", media)