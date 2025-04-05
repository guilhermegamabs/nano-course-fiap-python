with open("primeiro_arquivo.txt", "r") as arquivo:
    #conteudo = arquivo.readline() - readLine lê somente a primeira linha
    for linha in arquivo.readlines():
        print(linha)

