nome=input('Intoduza um nome: ')
nota1=float(input('Introduza a primeira nota: '))
nota2=float(input('introduza a segunda nota: '))
media=(nota1+nota2)/2
situacao='nula'

if media <8:
    situacao='Reprovado'
elif media >=8 and media <10:
    situacao='Recurso'
elif media >=10 and media <=20:
    situacao='Aprovado'
else:
    situacao='Não encontrada'

print(f'Aluno {nome}: Situacao {situacao}, a sua media foi de {media:.2f}')


nome=input('Intoduza o nome do segundo aluno: ')
nota1=float(input('Introduza a nota do segundo aluno primeira nota: '))
nota2=float(input('introduza a nota do segundo aluno segunda nota: '))
media=(nota1+nota2)/2
situacao='nula'

if media <8:
    situacao='Reprovado'
elif media >=8 and media <10:
    situacao='Recurso'
elif media >=10 and media <=20:
    situacao='Aprovado'
else:
    situacao='Não encontrada'

print(f'Aluno {nome}: Situacao {situacao}, a sua media foi de {media:.2f}')