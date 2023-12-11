
alunos = [
    {
    "nome": "dercio",
    "idade": 20, 
    "nota1": 12, 
    "nota2": 15
    }, 
    {
    "nome": "cassia",
    "idade": 20, 
    "nota1": 13, 
    "nota2": 14
    },
    {
    "nome": "Joao",
    "idade": 11, 
    "nota1": 11, 
    "nota2": 15
    }
    ]

for aluno in alunos:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2) / 2

    aluno["media"] = media

    print(f'A media do aluno {nome} eh {media}')


