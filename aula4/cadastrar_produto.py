file = open('produtos.txt', 'a')

for item in range(4):
    produto = input('Digite o nome do produto: ')
    file.write(f'{produto} \n')

file.close()