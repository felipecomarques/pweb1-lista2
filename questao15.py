lista = []
tamanho = int(input("Insira o tamanho da lista: "))

for i in range(tamanho):
    numero = int(input("Insira um numero: "))
    lista.append(numero)

numerox = int(input("Digite um numero para verificar se esta na lista: "))
if numerox in lista:
    print("O numero", numerox, "esta na lista")
else:
    print("O numero", numerox, "nao esta na lista")