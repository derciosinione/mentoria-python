file = open('produtos.txt', 'r')

frutas = []

for item in file:
    frutas.append(item.strip())

print(frutas)

file.close()