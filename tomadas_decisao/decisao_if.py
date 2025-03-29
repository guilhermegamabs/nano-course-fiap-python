nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))

if idade >= 65:
    print(f"O paciente {nome} possui atendimento preferencial")
else:
    print(f"O paciente {nome} não possui atendimento preferencial")