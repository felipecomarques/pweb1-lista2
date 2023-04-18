lista = []
tamanho = int(input("Insira o tamanho da lista: "))

for i in range(tamanho):
    numero = int(input("Insira um numero: "))
    lista.append(numero)

lista_cresente = sorted(lista)
print("A lista em ordem cresente eh:")
for i in lista_cresente:
    print(i)