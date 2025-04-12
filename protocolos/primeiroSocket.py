import socket

resp="S"
while(resp=="S"):
    url=input("Digite um URL: ")
    ip=socket.gethostbyname(url)
    print("O IP referente a url informada é: ", ip)
    resp=input("Digite <s> para continuar: ").upper()