tabuada = int(input("Digite um numero para exibir na tabuada: "))
print(f"Tabuada do número: {tabuada}")
for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))