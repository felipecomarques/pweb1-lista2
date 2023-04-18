numero = int(input("Insira um numero: "))
f0, f1, fi = 0,1,0

print("A sequencia de Fibonacci ate esse numero eh:")
for i in range(numero+1):
    fi = f0 + f1   
    f0 = f1
    f1 = fi
    print(fi, end=" ")