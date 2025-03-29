nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca=input("Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print(f"O paciente {nome} possui atendimento preferencial")
elif doenca=="SIM":
    print(f"O paciente {nome} deve ser direcionado para a sala de espera reservada")
else:
    print(f"O paciente {nome} não possui atendimento prioritário e pode aguardar na sala comum")