'''Faça um programa que guarda o nome de varios alunos e apresenta quantos alunos estão na lista
o programa deve solicitar ao utilizador quantos nomes pretende guardar
'''

alunos = []
quantidade = int(input('Quantos alunos pretende inserir na turma? '))

for item in range(0, quantidade):
  nome = input('Informa o nome do {}º aluno: '.format(item+1))
  alunos.append(nome)
  
tamanho = len(alunos)
print(f'Existem {tamanho} na turma')

alunos.insert(1,"Louco")

print(alunos)
alunos.sort()
print(alunos)

