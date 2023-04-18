numero = int(input("Insira um número: "))
f0, f1, fi = 0,1,0

print("A sequência de Fibonacci até esse número é:")
for i in range(numero+1):
    fi = f0 + f1   
    f0 = f1
    f1 = fi
    print(fi, end=" ")