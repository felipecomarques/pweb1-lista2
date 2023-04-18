lista = []
tamanho = int(input("Insira o tamanho da lista: "))

for i in range(tamanho):
    numero = int(input("Insira um numero: "))
    lista.append(numero)

print("O maior numero eh: ", max(lista))
print("O menor numero eh: ", min(lista))