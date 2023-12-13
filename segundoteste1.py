
def anos_aniversario(lista_pessoas : list[dict[str, str]]):
  dicionario_final = {}
  
  for dados in lista_pessoas:
    ano = dados.get('birthday').split('/')[-1]
    nome = dados.get('name')

    if(ano in dicionario_final):
      dicionario_final.get(ano).append(nome)
    else:
        dicionario_final[ano] = [nome]

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