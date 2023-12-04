# O dicionario funciona com chave e valor

aluno = {
    "nome": "dercio",
    "idade": 20, 
    # "nota1": 12, 
    # "nota2": 15,
    "notas": [12, 15]
}

print(aluno)

nome = aluno["nome"]
notas = aluno.get("notas")
nota1 = notas[0]
nota2 = notas[1]
media = (nota1 + nota2) / 2

aluno["media"] = media

aluno["nome"] = "Cassia Francisco"
 
print(f'A media do aluno {nome} eh {media}')

nova_lista_de_valor = list(aluno.keys())

print(f'Lista de valores: {nova_lista_de_valor}')
print(aluno)