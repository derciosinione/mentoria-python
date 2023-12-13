# def cria_aluno(alunos, cursos):
#   dicionarios = []
  
#   for indice in range(len(alunos)):
#     dados = {"nome":alunos[indice], "curso":cursos[indice]}
#     dicionarios.append(dados) 
  
#   return dicionarios 
    
# lista1 = ["Maria","ana", "derone", "Maria","ana", "derone", "Maria","ana", "derone", "Maria","ana", "derone"]
# lista2 = ["LEI","LIM", "INF", "LEI","LIM", "INF", "LEI","LIM", "INF", "LEI","LIM", "INF"]  

# print(cria_aluno(lista1,lista2))

# {'456': [jhdsjd]}


novo = {}

pessoa = {'name':'José', 'birthday':'25.11.1977'}
birthday = pessoa.get('birthday')
birthday = pessoa['birthday']
ano = birthday.split('.')[2]
ano2 = birthday.split('.')[-1]

# novo[ano] = []
# novo['43432'] = []
# novo[ano] = [123]

print(ano)
print(ano2)