def perguntar(): 
    return input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar usuários: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [
        input("Digite o nome: ").upper(),
        input("Digite a última data de acesso: "),
        input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)
    
def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ": " + str(valor))
    
def pesquisar(dicionario):
    login = input("Digite o login: ").upper()
    
    if(dicionario.get(login)):
        print("####-####")
        print("Usuário Encontrado:")
        print(f"Nome: {dicionario[login][0]}")
        print(f"Último Acesso: {dicionario[login][1]}")
        print(f"Estação: {dicionario[login][2]}\n")
    else:
        print("Usuário não encontrado.")
    
def excluir(dicionario):
    login = input("Digite o login: ").upper()

    if(dicionario.get(login)):
        del dicionario[login]
        print('Usuário excluído com sucesso.')
    else:
        print("Usuário não encontrado")        

def listar(dicionario):
    for usario in dicionario:
        print("####-####")
        print(f"Nome: {dicionario[usario][0]}")
        print(f"Último Acesso: {dicionario[usario][1]}")
        print(f"Estação: {dicionario[usario][2]}\n")