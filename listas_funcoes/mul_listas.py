equipamentos=[]
valores=[]
seriais=[]
departamentos=[]
resposta = "S"

while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

perg=input("Deseja buscar um equipamento específo?").upper()

if perg=="S":
    buscar=input("\nDigite o nome do equipamento que deseja buscar:")
    for indice in range(0, len(equipamentos)):
        if buscar==equipamentos[indice]:
            print("Departamento: ", departamentos[indice])
            print("Valor.......: ", valores[indice])
            print("Serial......: ", seriais[indice])
else:
    for item in range(0, len(equipamentos)):
        print("\nEquipamento..: ", (item+1))
        print("Nome.........: ", equipamentos[item])
        print("Valor........: ", valores[item])
        print("Serial.......: ", seriais[item])
        print("Departamento.: ", departamentos[item])