def cria_aluno(alunos, cursos):
  dicionarios = []
  
  for indice in range(len(alunos)):
    dados = {"nome":alunos[indice], "curso":cursos[indice]}
    dicionarios.append(dados) 
  
  return dicionarios 
    
lista1 = ["Maria","ana", "derone", "Maria","ana", "derone", "Maria","ana", "derone", "Maria","ana", "derone"]
lista2 = ["LEI","LIM", "INF", "LEI","LIM", "INF", "LEI","LIM", "INF", "LEI","LIM", "INF"]  

print(cria_aluno(lista1,lista2))

