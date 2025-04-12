import json
"""
#with open("C:/Users/zecro/OneDrive/Desktop/pythonNano/manipulacaoArquivos/bd.json", "r") as arq_json:
   dic = json.load(arq_json)
   for chave, dados in dic.items():
      print(chave + " " + str(dados))
"""   
with open("C:/Users/zecro/OneDrive/Desktop/pythonNano/manipulacaoArquivos/bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)