inventario=[]
resposta = "S"

while resposta=="S":
    equipamento=[input("Equipamento: "),
                 float(input("Valor: ")),
                int(input("Número Serial: ")),
                input(("Departamento: "))]
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

buscar=input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if buscar==elemento[0]:
         print("Valor..: ", elemento[1])
         print("Serial.: ", elemento[2])

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

serial = int(input("\nDigite o serial do equipamento que será excluído: "))
for elemento in inventario:
     if serial==elemento[2]:
          inventario.remove(elemento)

for elemento in inventario:
        print("Nome.........: ", equipamentos[0])
        print("Valor........: ", valores[1])
        print("Serial.......: ", seriais[2])
        print("Departamento.: ", departamentos[3])

valores=[]

for elemento in inventario:
     valores.append(elemento[1])
if len(valores)>0:
     print("O equipamento mais caro custa: ", max(valores))
     print("O equipamento mais barato custa: ", min(valores))
     print("O valor total dos equipamentos: ", sum(valores))