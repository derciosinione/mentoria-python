shopList = ["Cassia", "Joao", "Joel", "Naama", "Derone"]

shopList.append("Computador")
shopList.append("Pen-Drive")
shopList.append("Tablet")
shopList.append("Telefone")

print(shopList)

# list = original_list[start:stop:step]

# start é o índice do elemento inicial (inclusive),
# stop é o índice do elemento de parada (exclusivo),
# step é o tamanho do passo (o padrão é 1).

# print(shopList[0:9:3])

print(shopList[-3:])

print(shopList[:-3])

# elemento = input("Informe o elemento que pretendes eliminar: ")
# # Eliminar elemento da lista
# if(elemento in shopList):
#     shopList.remove(elemento)
# else:
#     print("O Elemento nao esta presente na lista")

# Eliminar pelo indice
# index = input("Informe o indice que pretendes eliminar: ")

# elemento = shopList.index(index)

# if(elemento in shopList):
#     shopList.remove(elemento)
# else:
#     print("O Elemento nao esta presente na lista")
# print(shopList)