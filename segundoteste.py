# 2. Faça uma função de nome anos_aniversario que recebe como argumento uma 
# lista de pessoas representadas por um dicionário com as chaves: ‘name’ e ‘birthday’ e 
# devolve um dicionário que deverá ter como chaves os anos em que há pessoas a fazer 
# anos e como valores uma lista com os nomes das pessoas que fazem anos nesse ano.
# >>>anos_aniversario([{‘name’:‘José’,‘birthday’:‘25/11/1977}, 
# {‘name’:‘Maria’,’birthday’:‘25/11/1986},{‘name’:’Pedro’, 
# ‘birthday’:‘25/10/1972},{‘name’:‘Afonso’,‘birthday’: ‘2/10/1972}])
# >>> {‘1977’:[‘Jose’], ‘1986’:[‘Maria], ‘1972’: [‘Pedro, ‘Afonso’]}

def anos_aniversario(lista_pessoas : list[dict[str, str]]):
  dicionario_final = {}
  nomes = []
  aniversarios = []
  
  for dados in lista_pessoas:
    ano = dados["birthday"].split('/')[-1]
    aniversarios.append(ano)
    nomes.append(dados["name"])
    dicionario_final[ano] = []

  for posicao in range(len(nomes)):
    if(aniversarios[posicao] in dicionario_final):
      dicionario_final[aniversarios[posicao]].append(nomes[posicao])      
  
  return dicionario_final
        
pessoas = [{'name':'José', 'birthday':'25/11/1977'}, 
           {'name': 'Maria','birthday':'25/11/1986'},
           {'name': 'Pedro', 'birthday':'25/10/1972'},
           {'name':'Afonso','birthday': '2/10/1972'},
           {'name':'Cassia', 'birthday':'25/11/1977'},
           {'name':'Joao', 'birthday':'25/11/1977'},
           {'name': 'Miguel','birthday':'25/11/1986'}, 
          ]

print(anos_aniversario(pessoas))