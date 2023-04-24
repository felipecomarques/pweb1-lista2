lista = []
tamanho = int(input("Insira o tamanho da lista: "))

for i in range(tamanho):
    numero = int(input("Insira um numero: "))
    lista.append(numero)

lista_decresente = sorted(lista, reverse=True)
print("A lista em ordem decresente eh:")
for i in lista_decresente:
    print(i)